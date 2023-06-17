```python
def system(x, t, u):
    """
    :param x: tuple of np.ndarray or torch.Tensor
    :param t: float
    :param u: np.ndarray or torch.Tensor
    :return: next x
    """
    x1, x2 = unpack(x)
    x1_next = x1 + TIME_STEP * x2
    x2_next = x2 + TIME_STEP * (-x1 + x2 + u)
    return x1_next, x2_next


def plot_vector_filed(fig, ax, f, title):
    space_num = 50
    X = mydata.grid(GLOBAL_RANGE, space_num)
    x1, x2 = unpack(X)
    if isinstance(f, nn.Module):
        x1_next, x2_next = mydata.use_net_as_func(f, (x1, x2))
    else:
        # f is just meth "system"
        x1_next, x2_next = f((x1, x2), 0., 0.)
    u = x1_next - x1
    v = x2_next - x2

    x1 = x1.reshape(space_num, space_num)
    x2 = x2.reshape(space_num, space_num)
    u = u.reshape(space_num, space_num)
    v = v.reshape(space_num, space_num)
    ax.streamplot(x1, x2, u, v, density=[1, 1])
    ax.grid()
    ax.set(title=title, aspect=1)
    plot_i_u_area(fig, ax)
    return


def show_vector_field(system, net_f, net_B=None):
    fig, ax = plt.subplots(ncols=2)
    plot_vector_filed(fig, ax[0], system, "original field")
    plot_vector_filed(fig, ax[1], net_f, "learned field")
    if net_B:
        plot_net_level(fig, ax[1], net_B)
    save_figure("field")
    plt.show()
    return
```

```python
plot.show_vector_field(system, net_f, net_B)
```

