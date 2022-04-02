class node:
    def __init__(self, id, X, Y, neighbor=[]) -> None:
        self.id = id
        self.X = X
        self.Y = Y

        # neighbours format: [{"name":Node, "distance":Number}, {"name":Node, "distance":Number}, ...]
        self.neighbor_nodes = neighbor[:]

        # routing_table format: {destinationId:(distance, nextHop), destinationId:(distance, nextHop), ...}
        self.routing_table = {}

        # neighbor_tables format: {id:routing_table, id:routing_table, ...}
        self.neighbor_tables = {}