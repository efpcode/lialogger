
def question_to_answer(question: str) -> str:
    bodytext_input = []

    print(f"\n>>> Enter your log for question: '{question}'\n\n>>> Exit by finish with an empty line.\n")

    while True:
        line = input()

        if not line.strip():
            bodytext_input.append(f"\n--- End: {question} ---\n\n")
            break
        bodytext_input.append(f"{line}\n")

    bodytext_input.insert(0, f"### {question}\n")
    return "\n".join(bodytext_input)
