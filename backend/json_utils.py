from typing import Any, Dict


def simple_message(message: str) -> Dict[str, str]:
    return {'msg': message}


def payload_data(payload: Dict[str, str]) -> Dict[str, Any]:
    return {'data': payload}
