class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = [0]

        for key in keys:
            for new_key in rooms[key]:
                if new_key not in keys:
                    keys.append(new_key)

        return len(keys) == len(rooms)

        

