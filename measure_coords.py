from PIL import Image

img = Image.open("assets/studio.png")
W, H = img.size
print(f"Image size: {W}x{H}")

# Let's verify our key regions:
# 1. Bookshelf on Left:
# Starts at x=50 (2.6%), y=140 (13.0%), width=460 (24.0%), height=820 (76.0%)
print("Bookshelf rect:", {"x": round(50/W*100, 1), "y": round(140/H*100, 1), "w": round(460/W*100, 1), "h": round(820/H*100, 1)})

# 2. Diploma inside Bookshelf:
# x=115 (6.0%), y=500 (46.3%), w=220 (11.5%), h=155 (14.3%)
print("Diploma rect:", {"x": round(115/W*100, 1), "y": round(500/H*100, 1), "w": round(220/W*100, 1), "h": round(155/H*100, 1)})

# 3. Portrait on Wall:
# x=595 (31.0%), y=280 (25.9%), w=150 (7.8%), h=190 (17.6%)
print("Portrait rect:", {"x": round(595/W*100, 1), "y": round(280/H*100, 1), "w": round(150/W*100, 1), "h": round(190/H*100, 1)})

# 4. Neural Schematic Poster:
# x=815 (42.4%), y=260 (24.1%), w=330 (17.2%), h=210 (19.4%)
print("Circuit rect:", {"x": round(815/W*100, 1), "y": round(260/H*100, 1), "w": round(330/W*100, 1), "h": round(210/H*100, 1)})

# 5. Floating Hologram Screens on Desk:
# x=680 (35.4%), y=485 (44.9%), w=520 (27.1%), h=195 (18.1%)
print("Hologram screens rect:", {"x": round(680/W*100, 1), "y": round(485/H*100, 1), "w": round(520/W*100, 1), "h": round(195/H*100, 1)})

# 6. Floating Classroom Board on Window:
# x=1385 (72.1%), y=345 (31.9%), w=410 (21.4%), h=305 (28.2%)
print("Classroom board rect:", {"x": round(1385/W*100, 1), "y": round(345/H*100, 1), "w": round(410/W*100, 1), "h": round(305/H*100, 1)})

# 7. AI Drone:
# x=1230 (64.1%), y=435 (40.3%), w=115 (6.0%), h=105 (9.7%)
print("AI Drone rect:", {"x": round(1230/W*100, 1), "y": round(435/H*100, 1), "w": round(115/W*100, 1), "h": round(105/H*100, 1)})
