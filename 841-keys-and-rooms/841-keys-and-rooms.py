class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        count = len(rooms)
        visited = set()
        def visit(room):
            if room not in visited:
                visited.add(room)
                for r in rooms[room]:
                    visit(r)
        visit(0)
        for i in range(count):
            if i not in visited:
                return False
        return True