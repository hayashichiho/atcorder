def replace_template(template_info: list[str], replacer_info: list[list[str]]) -> list[str]:
    base_tokens = " ".join(template_info).split()  # テンプレートをスペース区切りでトークン化
    results: list[str] = []

    # 各置換ルールセットに対してテンプレートを置換
    for rules in replacer_info:
        current_tokens = base_tokens[:]

        for i in range(0, len(rules), 2):
            old = rules[i]
            new = rules[i + 1]
            current_tokens = [new if token == old else token for token in current_tokens]

        # 置換後のトークンに "#" が含まれているかチェック
        if any(token.startswith("#") for token in current_tokens):
            results.append("Error: Lack of data")
        else:
            results.append(" ".join(current_tokens))

    return results
