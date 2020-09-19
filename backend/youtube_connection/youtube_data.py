from typing import Any, Dict
import json


class YoutubeData:
    def __init__(self, json_data: Dict[str, Any]):
        self.__total_results: int = json_data.get("pageInfo", {}).get("totalResults", 0)

        # TODO: filter by 'Official Video'
        # For now, save the first result
        self.__result: Dict[str, Any] = json_data.get("items", [{}])[0]
        self.__video_id: str = self.__result.get("id", {}).get("videoId", "")
        self.__video_title: str = self.__result.get("snippet", {}).get("title", "")

    @property
    def video_id(self) -> str:
        return self.__video_id

    @property
    def video_title(self) -> str:
        return self.__video_title

    def to_json(self) -> Dict[str, str]:
        return {
            'id': self.__video_id,
            'title': self.__video_title
        }
