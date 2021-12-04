def item_prefix(text: str, prefix='»') -> str:
    return f'{prefix} {text}'


def item_postfix(text: str, postfix: str) -> str:
    return f'{text} [{postfix}]'


def get_proxy_item_name(item_name: str, parent_name: str) -> str:
    text_with_prefix = item_prefix(item_name)
    return f'{item_postfix(text_with_prefix, parent_name) if item_name != parent_name else text_with_prefix}'
