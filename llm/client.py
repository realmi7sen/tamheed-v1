import asyncio

from anthropic import AsyncAnthropic

from utils.errors import LLMTimeoutError
from utils.types import ResponseLength


MODEL_NAME = "claude-haiku-4-5-20251001"
REQUEST_TIMEOUT = 60.0

MAX_TOKENS_BY_LENGTH = {
    ResponseLength.SHORT: 800,
    ResponseLength.NORMAL: 2000,
    ResponseLength.LONG: 4000,
}


class TamheedLLMClient:
    def __init__(self, client: AsyncAnthropic | None = None):
        self._client = client or AsyncAnthropic()

    async def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        response_length: ResponseLength,
    ) -> str:
        max_tokens = MAX_TOKENS_BY_LENGTH.get(response_length, 2000)
        try:
            message = await asyncio.wait_for(
                self._client.messages.create(
                    model=MODEL_NAME,
                    max_tokens=max_tokens,
                    system=system_prompt,
                    messages=[{"role": "user", "content": user_prompt}],
                ),
                timeout=REQUEST_TIMEOUT,
            )
        except asyncio.TimeoutError as error:
            raise LLMTimeoutError("انتهت مهلة الاتصال بالنموذج.") from error
        return message.content[0].text