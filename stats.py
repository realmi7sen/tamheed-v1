from database.db import TamheedDB

db = TamheedDB()

with db.connection() as conn:
    total = conn.execute("SELECT COUNT(*) FROM student_signals").fetchone()[0]
    users = conn.execute("SELECT COUNT(DISTINCT user_id) FROM student_signals").fetchone()[0]
    print(f"signals: {total} | users: {users}\n")

    print("--- score distribution ---")
    for row in conn.execute("""
        SELECT
          CASE
            WHEN retrieval_score < 0.5 THEN 'miss  <0.5'
            WHEN retrieval_score < 0.7 THEN 'weak  0.5-0.7'
            ELSE 'good  >0.7'
          END AS band,
          COUNT(*) AS n
        FROM student_signals GROUP BY band ORDER BY band
    """):
        print(f"  {row['band']:<16} {row['n']}")

    print("\n--- topics by avg score ---")
    for row in conn.execute("""
        SELECT topic, COUNT(*) n, ROUND(AVG(retrieval_score),3) avg
        FROM student_signals WHERE topic IS NOT NULL AND topic != ''
        GROUP BY topic ORDER BY avg ASC
    """):
        print(f"  {row['avg']}  n={row['n']:<4} {row['topic']}")

    print("\n--- teaching modes ---")
    for row in conn.execute("""
        SELECT teaching_mode, COUNT(*) n FROM student_signals
        GROUP BY teaching_mode ORDER BY n DESC
    """):
        print(f"  {row['n']:<4} {row['teaching_mode']}")

    print("\n--- last 15 ---")
    for row in conn.execute("""
        SELECT user_id, topic, teaching_mode, retrieval_score, was_followup, created_at
        FROM student_signals ORDER BY id DESC LIMIT 15
    """):
        print(f"  {row['created_at']} u{row['user_id']} {row['retrieval_score']:.3f} "
              f"fu={row['was_followup']} [{row['teaching_mode']}] {row['topic']}")

    print("\n--- students ---")
    for row in conn.execute("""
        SELECT user_id, username, first_name, total_questions, first_seen, last_seen
        FROM students ORDER BY total_questions DESC
    """):
        print(f"  u{row['user_id']} @{row['username']:<15} q={row['total_questions']:<4} "
              f"first={row['first_seen']} last={row['last_seen']}")