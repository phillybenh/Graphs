            #####

            # if self.current_room not in self.graph:
            #     # visited += 1
            #     self.graph[self.current_room] = {}
            #     exits = player.current_room.get_exits()
            #     for e in exits:
            #         self.graph[self.current_room].update({e: '?'})

            #####

            # print("first room", player.current_room)
            # player.travel('n')
            # player.travel('n')
            # print("second room", player.current_room.id)
            # print("exits", player.current_room.get_exits())

    #   # else, backtrack to last room with a new exit
    #   else:
    #        # TODO: implement a BFS or some way back to a room unexplored
    #        backtrack_count = 1
    #         moves = self.available_moves()
    #          while moves is False:
    #               back_direction = self.path[-backtrack_count]
    #                if back_direction == 'n':
    #                     direction = 's'
    #                 elif back_direction == 'e':
    #                     direction = 'w'
    #                 elif back_direction == 's':
    #                     direction = 'n'
    #                 elif back_direction == 'w':
    #                     direction = 'e'
    #                 else:
    #                     print("You broke something in backtrack")

    #                 self.current_room = player.current_room.id
    #                 player.travel(direction)
    #                 self.path.append(direction)
    #                 backtrack_count -= 2
    #                 moves = self.available_moves()
