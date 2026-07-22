import asyncio

from anthropic import AsyncAnthropic

from utils.errors import LLMTimeoutError
from utils.types import ResponseLength


MODEL_NAME = "claude-haiku-4-5-20251001"
REQUEST_TIMEOUT = 60.0

MAX_TOKENS_BY_LENGTH = {
    ResponseLength.SHORT: 550,
    ResponseLength.NORMAL: 2000,
    ResponseLength.LONG: 4000,
}


class TamheedLLMClient:
    def __init__(self, client: AsyncAnthropic | None = None):
        self._client = client or AsyncAnthropic()

    async def generate(
        self,
        base_prompt: str,
        variable_prompt: str,
        user_prompt: str,
        response_length: ResponseLength,
        history: list | None = None,
        enable_cache: bool = False,
    ) -> str:
        max_tokens = MAX_TOKENS_BY_LENGTH.get(response_length, 2000)

        messages = list(history) if history else []
        messages.append({"role": "user", "content": user_prompt})

        # ===============================
        # Build system prompt
        # ===============================
        base_block = {"type": "text", "text": base_prompt}
        if enable_cache:
            base_block["cache_control"] = {"type": "ephemeral"}
        system_blocks = [
            base_block,
            {"type": "text", "text": variable_prompt},
        ]

        system_blocks.append(base_block)

        system_blocks.append(
            {
                "type": "text",
                "text": variable_prompt,
            }
        )

        try:
            message = await asyncio.wait_for(
                self._client.messages.create(
                    model=MODEL_NAME,
                    max_tokens=max_tokens,
                    system=system_blocks,
                    messages=messages,
                ),
                timeout=REQUEST_TIMEOUT,
            )

        except asyncio.TimeoutError as error:
            raise LLMTimeoutError("انتهت مهلة الاتصال بالنموذج.") from error

        print(
            f"[CACHE] created={message.usage.cache_creation_input_tokens} "
            f"read={message.usage.cache_read_input_tokens} "
            f"input={message.usage.input_tokens}"
        )

        if not message.content or not message.content[0].text:
            raise LLMTimeoutError("النموذج رجع رد فاضي.")

        return message.content[0].text