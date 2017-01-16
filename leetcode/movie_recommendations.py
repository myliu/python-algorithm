# RETURN AN EMPTY LIST IF NO SIMILAR MOVIE TO THE GIVEN MOVIE IS FOUND
import heapq

def getMovieRecommendations(movie, N):
    if not movie or not N:
        return []

    def dfs(movie, seen, heap):
        if movie.getId() in seen:
            return
        seen.add(movie.getId())
        # Python's heap is min-heap,
        # because we want to have the movie with large ratings come out first,
        # we use the minus sign to reverse the min-heap to max-heap
        heapq.heappush(heap, (-movie.getRating(), movie))
        for other in movie.getSimilarMovies():
            dfs(other, seen, heap)
    
    seen = set()
    heap = []
    dfs(movie, seen, heap)
    result = [heapq.heappop(heap)[1] for _ in range(min(len(heap), N))]
    return filter(lambda x:x.getId() != movie.getId(), result)