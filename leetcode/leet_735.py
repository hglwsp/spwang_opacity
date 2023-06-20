def asteroidCollision(asteroids):
    st = []
    for aster in asteroids:
        alive = True
        while alive and aster < 0 and st and st[-1] > 0:
            alive = st[-1] < -aster
            if st[-1] <= -aster:
                st.pop()
        if alive:
            st.append(aster)
    return st