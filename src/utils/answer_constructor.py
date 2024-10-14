from src.models.common_models import NameValueModel


def code_style_decorator(func):
    def wrapper(*args, **kwargs):
        original_msg = func(*args, **kwargs)
        code_style_msg = f"<code>{original_msg}</code>"
        return code_style_msg

    return wrapper


@code_style_decorator
def generate_simple_answer(msg: NameValueModel):
    name = f"{msg.name}"
    value = f"{msg.value}"

    return f"{name}\n" \
           f"{value}"


@code_style_decorator
def generate_multi_simple_answer(msgs: list[NameValueModel]):
    answer = ''
    for msg in msgs:
        answer += f'{msg.name}: {msg.value}\n'
    return answer


@code_style_decorator
def generate_str_answer(msg: str):
    return msg
