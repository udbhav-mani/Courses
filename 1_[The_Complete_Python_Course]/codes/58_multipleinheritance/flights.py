class Segments:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self) -> str:
        return f"{self.start} -> {self.end}"


class Flights:
    def __init__(self, segments):
        self.segments = segments

    def __repr__(self) -> str:
        seg = [self.segments[0].start, self.segments[0].end]
        for segment in self.segments[1:]:
            seg.append(segment.end)

        return " -> ".join(seg)

    @property
    def start_destination(self):
        print(self.segment[0].start)

    @start_destination.setter
    def start_destination(self, value):
        self.segment[0].start = value


segment1 = Segments("IND", "GLA")
segment2 = Segments("GLA", "PUN")


segments = []
segments.append(segment1)
segments.append(segment2)

flight = Flights(segments=segments)
print(flight)
