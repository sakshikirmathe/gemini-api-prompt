class ResponseParser:
    def parse(self, response: str) -> dict:
        return {
            "raw_output": response,
            "character_count": len(response),
            "preview": response[:200]
        }
