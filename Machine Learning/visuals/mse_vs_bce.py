"""Why logistic regression uses BCE, not MSE: loss landscapes + per-sample loss and gradient."""
import numpy as np
import matplotlib.pyplot as plt

MSE_C, BCE_C = "#eb6834", "#2a78d6"
INK, MUTED, GRID = "#1f1f1e", "#6b6a63", "#e6e5e0"
sig = lambda z: 1 / (1 + np.exp(-z))

# Tiny 1-feature dataset, model p = sigmoid(w * x) (no bias, so the loss is a curve in w)
x = np.array([-3.0, -0.3, 0.1, 0.4])
y = np.array([0, 1, 1, 0])
w = np.linspace(-7, 4, 2000)
P = sig(np.outer(w, x))
eps = 1e-12
mse = ((P - y) ** 2).mean(1)
bce = -(y * np.log(P + eps) + (1 - y) * np.log(1 - P + eps)).mean(1)

def grad(f, w0, h=1e-5):
    return (f(w0 + h) - f(w0 - h)) / (2 * h)

def mse_f(w0):
    p = sig(w0 * x); return ((p - y) ** 2).mean()

def bce_f(w0):
    p = sig(w0 * x); return -(y * np.log(p + eps) + (1 - y) * np.log(1 - p + eps)).mean()

def descend(f, w0, lr, steps):
    path = [w0]
    for _ in range(steps):
        w0 = w0 - lr * grad(f, w0); path.append(w0)
    return np.array(path)

start = -3.0
mse_path = descend(mse_f, start, lr=2.0, steps=300)
bce_path = descend(bce_f, start, lr=0.5, steps=300)

plt.rcParams.update({"font.size": 11, "axes.edgecolor": MUTED, "axes.labelcolor": INK,
                     "xtick.color": MUTED, "ytick.color": MUTED, "axes.spines.top": False,
                     "axes.spines.right": False, "axes.grid": True, "grid.color": GRID})
fig, ax = plt.subplots(2, 2, figsize=(13, 9))

def landscape(a, loss, f, path, color, title):
    a.plot(w, loss, color=color, lw=2)
    show = path[::max(1, len(path) // 25)]
    a.scatter(show, [f(v) for v in show], s=28, color=color, edgecolor="white", lw=1.2, zorder=3)
    a.scatter([path[0]], [f(path[0])], s=90, marker="o", facecolor="white", edgecolor=INK, lw=1.5, zorder=4)
    a.annotate("start (w = -3)", (path[0], f(path[0])), xytext=(10, 12), textcoords="offset points", color=INK)
    a.set_title(title, loc="left", color=INK, fontweight="bold")
    a.set_xlabel("weight w"); a.set_ylabel("loss")

landscape(ax[0, 0], mse, mse_f, mse_path, MSE_C, "MSE + sigmoid: non-convex")
i_loc = np.argmin(np.where(w < -2, mse, np.inf)); i_glob = np.argmin(mse)
ax[0, 0].annotate("local minimum:\ngradient descent gets stuck here", (w[i_loc], mse[i_loc]),
                  xytext=(-6.8, 0.31), color=INK, ha="left",
                  arrowprops=dict(arrowstyle="->", color=MUTED))
ax[0, 0].annotate("global minimum\n(never reached)", (w[i_glob], mse[i_glob]),
                  xytext=(-2.0, 0.235), color=INK, ha="right", va="center",
                  arrowprops=dict(arrowstyle="->", color=MUTED))

landscape(ax[0, 1], bce, bce_f, bce_path, BCE_C, "BCE + sigmoid: convex (one bowl)")
j = np.argmin(bce)
ax[0, 1].annotate("single minimum:\nreached from any start", (w[j], bce[j]),
                  xytext=(2.2, 2.3), color=INK, ha="center",
                  arrowprops=dict(arrowstyle="->", color=MUTED))

# Bottom row: one sample with true label y = 1, as a function of the score z = w.x + b
z = np.linspace(-8, 8, 800)
p = sig(z)
a = ax[1, 0]
a.plot(z, (1 - p) ** 2, color=MSE_C, lw=2, label="MSE: (1 - p)²")
a.plot(z, -np.log(p), color=BCE_C, lw=2, label="BCE: -log p")
a.set_ylim(0, 6)
a.set_title("Loss for one sample with y = 1", loc="left", color=INK, fontweight="bold")
a.set_xlabel("score z  (very negative = confidently wrong)"); a.set_ylabel("loss")
a.annotate("MSE caps at 1:\nvery wrong ≈ a bit wrong", (-6.5, 1), xytext=(-7.8, 0.45), color=INK, va="center",
           arrowprops=dict(arrowstyle="->", color=MUTED))
a.annotate("BCE keeps growing:\nbig mistakes cost a lot", (-5, 5), xytext=(-2.2, 4.8), color=INK,
           arrowprops=dict(arrowstyle="->", color=MUTED))
a.legend(frameon=False, loc="upper right")

a = ax[1, 1]
a.plot(z, 2 * (1 - p) * p * (1 - p), color=MSE_C, lw=2, label="MSE gradient")
a.plot(z, 1 - p, color=BCE_C, lw=2, label="BCE gradient")
a.set_title("How hard the gradient pushes (y = 1)", loc="left", color=INK, fontweight="bold")
a.set_xlabel("score z"); a.set_ylabel("|dLoss / dz|")
a.annotate("MSE: push → 0\nwhen very wrong\n(learning stalls)", (-6, 0.005), xytext=(-7.8, 0.4),
           color=INK, arrowprops=dict(arrowstyle="->", color=MUTED))
a.annotate("BCE: push = (1 - p) → 1\nwhen very wrong", (-6, 0.997), xytext=(1.0, 0.85), color=INK,
           arrowprops=dict(arrowstyle="->", color=MUTED))
a.legend(frameon=False, loc="center right")

fig.suptitle("Why logistic regression uses BCE (log loss), not MSE", x=0.01, ha="left",
             fontsize=15, fontweight="bold", color=INK)
fig.tight_layout()
fig.savefig(__file__.replace(".py", ".png"), dpi=150, facecolor="white")
print("MSE ends at w =", round(mse_path[-1], 2), "| BCE ends at w =", round(bce_path[-1], 2),
      "| MSE global min at w =", round(w[i_glob], 2))
