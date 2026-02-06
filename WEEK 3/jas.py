import heapq
G=((1,2,3),(4,5,6),(7,8,0))
H=lambda s:sum(abs(i-(v-1)//3)+abs(j-(v-1)%3) for i in range(3) for j in range(3) if (v:=s[i][j]))
N=lambda s:[tuple(tuple(s[i][j] if (i,j)!=(x,y) else s[nx][ny] if (i,j)==(x,y) else 0
    for j in range(3)) for i in range(3))
    for x,y in [(i,j) for i in range(3) for j in range(3) if s[i][j]==0]
    for nx,ny in [(x+dx,y+dy) for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]] if 0<=nx<3 and 0<=ny<3]
def A(s):
    q,v=[(H(s),0,s)],{s:None}
    while q:
        _,g,s=heapq.heappop(q)
        if s==G: return g
        for n in N(s):
            if n not in v: v[n]=s; heapq.heappush(q,(g+1+H(n),g+1,n))
print(A(((1,2,3),(4,0,6),(7,5,8))))
