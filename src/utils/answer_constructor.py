from src.models.common_models import NameValueModel


def code_style_decorator(func):
    def wrapper():
        original_msg = func()
        code_style_msg = f"```{original_msg}```"
        return code_style_msg
    return wrapper


def generate_simple_answer(msg: NameValueModel):
    name = f"{msg.name}"
    value = f"{msg.value}"

    return f"{name}\n" \
           f"{value}"


def generate_str_answer(msg: str):
    return msg
