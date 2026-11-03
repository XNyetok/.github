#!/usr/bin/env python3
"""Builds the banner and buttons that profile/README.md shows, each in a light and a dark variant.

Run it from anywhere after changing their text or colors:

    python3 scripts/build-profile-assets.py

It writes profile/assets/<name>-light.svg and <name>-dark.svg. The README picks the variant that matches the
viewer's theme with <picture>. Only the standard library is used.

The look follows nyetok.id (docs/design.md in the website's repository): a soft gray page between hairline rails,
small square marks where the lines cross, a sans headline with an italic serif second line, line drawings, and
Nyetok magenta for actions. GitHub draws SVG text with the viewer's own fonts, so the serif line falls back to
Iowan Old Style on a Mac and to Palatino or Georgia elsewhere. Text inside an SVG doesn't wrap: every line is
set by hand, so keep lines about as long as they are now.
"""

from html import escape
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "profile" / "assets"

# Light is nyetok.id's own palette; dark uses GitHub's dark colors, so the banner sits naturally on either page.
THEMES = {
    "light": {
        "page": "#f3f3f1", "panel": "#ffffff", "soft": "#ececea", "ink": "#111111", "text2": "#4a4a4a",
        "text3": "#686866", "accent": "#b8005f", "line": 0.10, "mark": 0.26, "art": 0.88, "plate": 0.22,
        "edge": 0, "button": "#ffffff", "button_line": 0.14,
    },
    "dark": {
        "page": "#161b22", "panel": "#0d1117", "soft": "#21262d", "ink": "#e6edf3", "text2": "#9198a1",
        "text3": "#7d8590", "accent": "#ff4d9e", "line": 0.13, "mark": 0.32, "art": 0.8, "plate": 0.25,
        "edge": 0.14, "button": "#21262d", "button_line": 0.18,
    },
}
MAGENTA = "#d6006f"  # the logo, the sparkles and the primary button, in both themes
HAVUS_INK = "#0b0b0c"

SANS = '"Inter",-apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans",Helvetica,Arial,sans-serif'
MONO = 'ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,"Liberation Mono",monospace'
SERIF = '"Instrument Serif","Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif'
BASE_CSS = (
    f"text{{font-family:{SANS}}}.mono{{font-family:{MONO}}}.serif{{font-family:{SERIF};font-style:italic}}"
    ".grow{transform-box:fill-box;transform-origin:center}"
    "@media (prefers-reduced-motion:reduce){*{animation:none!important}}"
)

# Helvetica/Arial advance widths (1/1000 em): a safe upper bound for the system sans fonts.
_W = dict(zip(" !\"#$%&'()*+,-./0123456789:;<=>?@", [278, 278, 355, 556, 556, 889, 667, 191, 333, 333, 389, 584,
          278, 333, 278, 278] + [556] * 10 + [278, 278, 584, 584, 584, 556, 1015]))
_W.update(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", [667, 667, 722, 722, 667, 611, 778, 722, 278, 500, 667, 556, 833, 722,
          778, 667, 778, 722, 667, 611, 722, 667, 944, 667, 667, 611]))
_W.update(zip("abcdefghijklmnopqrstuvwxyz", [556, 556, 500, 556, 556, 278, 556, 556, 222, 222, 500, 222, 833, 556,
          556, 556, 556, 333, 500, 278, 556, 500, 722, 500, 500, 500]))
_W.update({"·": 278, "’": 222})


def width(text, size, *, bold=False, mono=False, spacing=0.0):
    """Estimated rendered width of a line of text, in SVG units."""
    if mono:
        base = 0.6 * size * len(text)
    else:
        base = sum(_W.get(ch, 556) for ch in text) / 1000 * size * (1.07 if bold else 1.0)
    return base + spacing * len(text)


def svg(w, h, label, body, defs="", css=""):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
        f'role="img" aria-label="{escape(label)}"><title>{escape(label)}</title>'
        f"<style>{BASE_CSS}{css}</style><defs>{defs}</defs>{body}</svg>\n"
    )


def text(x, y, content, *, size, fill, weight=None, cls=None, spacing=None, anchor=None, extra=""):
    attrs = [f'x="{x:g}"', f'y="{y:g}"', f'font-size="{size:g}"', f'fill="{fill}"']
    if cls:
        attrs.append(f'class="{cls}"')
    if weight:
        attrs.append(f'font-weight="{weight}"')
    if spacing is not None:
        attrs.append(f'letter-spacing="{spacing:g}"')
    if anchor:
        attrs.append(f'text-anchor="{anchor}"')
    if extra:
        attrs.append(extra)
    return f'<text {" ".join(attrs)}>{content}</text>'


# The rounded square that the Nyetok logo and the Havus icon share, on their 1024-unit grid (it spans 100 to 924).
SQUIRCLE = ("M396.64 100h230.72c103.83 0 155.75 0 195.41 20.21a185.4 185.4 0 0 1 81.02 81.02C924 240.89 924 292.81 924 "
            "396.64v230.72c0 103.83 0 155.75-20.21 195.41a185.4 185.4 0 0 1-81.02 81.02C783.11 924 731.19 924 627.36 "
            "924H396.64c-103.83 0-155.75 0-195.41-20.21a185.4 185.4 0 0 1-81.02-81.02C100 783.11 100 731.19 100 "
            "627.36V396.64c0-103.83 0-155.75 20.21-195.41a185.4 185.4 0 0 1 81.02-81.02C240.89 100 292.81 100 "
            "396.64 100Z")
# Nyetok: an N split by a 70° cut (design/logo.svg in the website's repository).
NYETOK_N = ("M288 728V288h104l129.98 151.64-40.88 112.31L392 448v280ZM736 296v440H632L502.02 584.36l40.88-112.31L632 "
            "576V296Z")
# Havus: an H split by the same cut (design/AppIcon.svg in XNyetok/Havus).
HAVUS_H = "M288 288H392V464H514.57L482.54 552H392V728H288ZM736 736H632V560H509.43L541.46 472H632V296H736Z"


def logo(t, x, y, size, tile, glyph, *, edge=False):
    """A logo or app icon on its rounded square, top-left corner at x, y. `edge` outlines a dark tile in dark mode."""
    k = size / 824
    stroke = (f' stroke="#fff" stroke-opacity="{t["edge"]}" stroke-width="{1 / k:.1f}"' if edge and t["edge"] else "")
    return (f'<g transform="translate({x:g} {y:g}) scale({k:.5f}) translate(-100 -100)">'
            f'<path d="{SQUIRCLE}" fill="{tile}"{stroke}/><path d="{glyph}" fill="#fff"/></g>')


def sparkle(cx, cy, r, color, extra=""):
    """A four-point star, like the ones that twinkle on nyetok.id."""
    a = r * 0.16
    pts = [(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)]
    ctl = [(cx + a, cy - a), (cx + a, cy + a), (cx - a, cy + a), (cx - a, cy - a)]
    d = f"M{pts[0][0]:g} {pts[0][1]:g}" + "".join(
        f"C{ctl[i][0]:g} {ctl[i][1]:g} {ctl[i][0]:g} {ctl[i][1]:g} {pts[(i + 1) % 4][0]:g} {pts[(i + 1) % 4][1]:g}"
        for i in range(4)
    )
    return f'<path d="{d}Z" fill="{color}"{extra}/>'


def arrow(cx, cy, color, size=10):
    """A "goes somewhere" arrow, centered on cx, cy."""
    h = size / 2
    return (f'<path d="M{cx - h:g} {cy + h:g}L{cx + h:g} {cy - h:g}'
            f'M{cx - h + 2.6:g} {cy - h:g}H{cx + h:g}V{cy + h - 2.6:g}" '
            f'fill="none" stroke="{color}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>')


# ----------------------------------------------------------------------------------------------- drawing


def strokes(t, *, dashed=False, line=1.6, fade=1.0):
    """The drawings' pen: ink, round ends; `fade` lightens it, `dashed` draws what isn't there yet."""
    return (f'stroke="{t["ink"]}" stroke-opacity="{t["art"] * fade:.2f}" stroke-width="{line:g}" '
            'stroke-linejoin="round" stroke-linecap="round"' + (' stroke-dasharray="4 4"' if dashed else ""))


def plate(t, x, y, w, label, dashed=False):
    """The box's label: a small card with the app's name in caps."""
    dash = ' stroke-dasharray="3 3"' if dashed else ""
    return (f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="20" rx="4" fill="{t["page"]}" stroke="{t["ink"]}" '
            f'stroke-opacity="{t["plate"]}"{dash}/>'
            + text(x + w / 2 + 0.8, y + 14, label, size=11, fill=t["text3"] if dashed else t["ink"], weight=700,
                   cls="mono", spacing=1.6, anchor="middle"))


def closed_box(t, x, floor, w, h, label):
    """A taped box seen from a little above, stamped with the Nyetok logo."""
    top, mid = floor - h, x + w / 2
    return (
        f'<path d="M{x + 9:g} {top - 12:g}H{x + w - 9:g}L{x + w:g} {top:g}H{x:g}Z" fill="{t["soft"]}" {strokes(t)}/>'
        f'<path d="M{mid - 7:g} {top - 12:g}H{mid + 7:g}L{mid + 9:g} {top:g}H{mid - 9:g}Z" fill="{t["panel"]}" '
        f'{strokes(t, line=1)}/>'
        f'<rect x="{x:g}" y="{top:g}" width="{w:g}" height="{h:g}" rx="4" fill="{t["panel"]}" {strokes(t)}/>'
        f'<path d="M{mid - 9:g} {top:g}V{top + 12:g}H{mid + 9:g}V{top:g}" fill="{t["soft"]}" {strokes(t, line=1)}/>'
        + plate(t, x + 18, top + 22, w - 36, label)
        + logo(t, x + w - 21, floor - 21, 13, MAGENTA, NYETOK_N)
    )


def open_box(t, x, floor, w, h, label, contents):
    """An open box with its flaps out; `contents` is drawn inside it, so the front hides its lower part."""
    top = floor - h
    bl, br = (x + 9, top - 12), (x + w - 9, top - 12)
    s = strokes(t)
    return (
        f'<path d="M{bl[0]:g} {bl[1]:g}H{br[0]:g}L{br[0] - 7:g} {br[1] - 15:g}H{bl[0] + 7:g}Z" '
        f'fill="{t["panel"]}" {s}/>'
        f'<path d="M{bl[0]:g} {bl[1]:g}H{br[0]:g}L{x + w:g} {top:g}H{x:g}Z" fill="{t["soft"]}" {s}/>'
        + contents
        + f'<path d="M{x:g} {top:g}L{bl[0]:g} {bl[1]:g}L{bl[0] - 24:g} {bl[1] - 5:g}L{x - 26:g} {top - 3:g}Z" '
        f'fill="{t["panel"]}" {s}/>'
        f'<path d="M{x + w:g} {top:g}L{br[0]:g} {br[1]:g}L{br[0] + 24:g} {br[1] - 5:g}L{x + w + 26:g} {top - 3:g}Z" '
        f'fill="{t["panel"]}" {s}/>'
        f'<rect x="{x:g}" y="{top:g}" width="{w:g}" height="{h:g}" rx="4" fill="{t["panel"]}" {s}/>'
        + plate(t, x + 18, top + 22, w - 36, label)
        + logo(t, x + w - 21, floor - 21, 13, MAGENTA, NYETOK_N)
    )


def next_box(t, x, floor, w, h):
    """The next app's box: still empty, drawn in dashes."""
    top = floor - h
    s = strokes(t, dashed=True, fade=0.55)
    return (f'<path d="M{x + 8:g} {top - 11:g}H{x + w - 8:g}L{x + w:g} {top:g}H{x:g}Z" fill="none" {s}/>'
            f'<rect x="{x:g}" y="{top:g}" width="{w:g}" height="{h:g}" rx="4" fill="none" {s}/>'
            + plate(t, x + 14, top + 16, w - 28, "NEXT", dashed=True))


# ------------------------------------------------------------------------------------------------ banner


def banner(t):
    W, H = 1000, 320
    ink, page = t["ink"], t["page"]
    rails, nav, foot = (36, 964), 72, 256
    hair = f'stroke="{ink}" stroke-opacity="{t["line"]}"'
    defs = '<clipPath id="c"><rect x="8" y="8" width="984" height="304" rx="24"/></clipPath>'
    # Hairline rails and dividers, with a small outlined square wherever they cross.
    lines = (f'<g clip-path="url(#c)" fill="none" {hair}>'
             + "".join(f'<path d="M{x} 8V312"/>' for x in rails)
             + "".join(f'<path d="M8 {y}H992"/>' for y in (nav, foot)) + "</g>"
             + "".join(f'<rect x="{x - 3.5}" y="{y - 3.5}" width="7" height="7" fill="{page}" stroke="{ink}" '
                       f'stroke-opacity="{t["mark"]}"/>' for x in rails for y in (nav, foot)))

    # The nav: logo and wordmark on the left, the magenta button on the right.
    label = "nyetok.id"
    bw = 18 + width(label, 14.5, bold=True) + 12 + 28 + 5
    bx = 940 - bw
    nav_bar = (
        logo(t, 60, 25, 30, MAGENTA, NYETOK_N)
        + text(100, 49.5, "Nyetok", size=24, fill=ink, weight=650, spacing=-0.96)
        + f'<rect x="{bx:.1f}" y="21" width="{bw:.1f}" height="38" rx="8" fill="{MAGENTA}"/>'
        + text(bx + 18, 45, label, size=14.5, fill="#fff", weight=600)
        + f'<rect x="{bx + bw - 33:.1f}" y="26" width="28" height="28" rx="6" fill="#fff"/>'
        + arrow(bx + bw - 19, 40, MAGENTA, 9)
    )

    # The words. The second line of the headline is the italic serif, as on every nyetok.id headline.
    words = (
        sparkle(66, 101, 5.5, MAGENTA)
        + text(80, 106, "SMALL APPS · MADE IN INDONESIA", size=12, fill=t["text3"], weight=600, cls="mono",
               spacing=1.8)
        + text(57, 156, "Stocking up on small apps", size=44, fill=ink, weight=500, spacing=-1.76)
        + text(59, 204, "that are actually useful.", size=49, fill=ink, cls="serif", spacing=-0.4)
        + text(60, 238, "Light, tidy and private apps for your Mac, free and open source.", size=16,
               fill=t["text2"])
    )

    # The recipe strip: what every app has, each set in a different face, like the strip on nyetok.id.
    recipe = [
        ("Native Swift", dict(size=15, weight=600)),
        ("MIT license", dict(size=14, cls="mono")),
        ("free", dict(size=19, cls="serif")),
        ("NO ACCOUNT", dict(size=12, weight=700, spacing=1.6)),
        ("No telemetry", dict(size=15, weight=500)),
    ]
    strip = text(60, 289, "SAME RECIPE, EVERY APP", size=11, fill=t["text3"], weight=600, cls="mono", spacing=1.6)

    def extent(word, style):
        size, spacing = style["size"], style.get("spacing", 0)
        if style.get("cls") == "mono":
            return width(word, size, mono=True, spacing=spacing)
        if style.get("cls") == "serif":
            return 0.4 * size * len(word)  # an italic serif runs narrower than the sans table
        return width(word, size, bold=style.get("weight", 400) >= 600, spacing=spacing)

    # Spread the words evenly between the label and the right rail's gutter, with a dot in each gap.
    left, right = 336, 940
    sizes = [extent(word, style) for word, style in recipe]
    gap = (right - left - sum(sizes)) / (len(recipe) - 1)
    x = left
    for i, ((word, style), w) in enumerate(zip(recipe, sizes)):
        strip += text(x + w / 2, 289, escape(word), fill=t["text3"], anchor="middle", **style)
        if i < len(recipe) - 1:
            strip += f'<circle cx="{x + w + gap / 2:.1f}" cy="284.5" r="1.6" fill="{t["text3"]}" fill-opacity=".6"/>'
        x += w + gap

    # The drawing: the apps in stock, standing on the bottom divider. Havus, the newest, pops out of the top box.
    floor = foot
    icon_x, icon_y = 702, 93
    havus = (f'<g class="bob"><g transform="rotate(-10 {icon_x + 23} {icon_y + 23})">'
             + logo(t, icon_x, icon_y, 46, HAVUS_INK, HAVUS_H, edge=True) + "</g></g>")
    sparkles = "".join(
        sparkle(cx, cy, r, MAGENTA, f' class="grow tw" style="animation-delay:{delay}s"')
        for cx, cy, r, delay in [(776, 98, 7.5, 0), (667, 103, 4.6, 0.8), (824, 111, 3.6, 1.5)]
    )
    art = (
        closed_box(t, 612, floor, 110, 58, "XSPACE")
        + closed_box(t, 728, floor, 110, 58, "JAMBUL")
        + open_box(t, 670, floor - 62, 110, 58, "HAVUS", havus)
        + sparkles
        + next_box(t, 856, floor, 84, 48)
    )

    body = (
        f'<rect x="8" y="8" width="984" height="304" rx="24" fill="{page}" stroke="{ink}" '
        f'stroke-opacity="{t["line"] * 1.4:.2f}"/>'
        + lines + nav_bar + words + strip + art
    )
    css = (
        "@keyframes bob{0%,100%{transform:translateY(0)}50%{transform:translateY(-4px)}}"
        ".bob{animation:bob 3.6s ease-in-out infinite}"
        "@keyframes tw{0%,100%{opacity:.3;transform:scale(.55)}50%{opacity:1;transform:scale(1)}}"
        ".tw{animation:tw 2.8s ease-in-out infinite both}"
    )
    alt = ("Nyetok: stocking up on small apps that are actually useful. Light, tidy and private apps for your Mac, "
           "free and open source, made in Indonesia. The same recipe in every app: native Swift, MIT license, free, "
           "no account, no telemetry. nyetok.id")
    return svg(W, H, alt, body, defs, css)


# ----------------------------------------------------------------------------------------------- buttons


def button(t, label, primary=False):
    """nyetok.id's button: a label and a square chip with an arrow. Magenta for the main action, white for the rest."""
    lw = width(label, 15, bold=True)
    bw = 20 + lw + 14 + 30 + 6
    W, H = round(bw + 8), 66
    fill, ink = (MAGENTA, "#ffffff") if primary else (t["button"], t["ink"])
    chip_fill, chip_ink = ("#ffffff", MAGENTA) if primary else (t["ink"], t["button"])
    outline = "" if primary else f' stroke="{t["ink"]}" stroke-opacity="{t["button_line"]}"'
    body = (
        f'<rect x="4" y="10" width="{bw:.1f}" height="46" rx="8" fill="{fill}"{outline}/>'
        + text(24, 38.5, escape(label), size=15, fill=ink, weight=600)
        + f'<rect x="{4 + bw - 36:.1f}" y="18" width="30" height="30" rx="6" fill="{chip_fill}"/>'
        + arrow(4 + bw - 21, 33, chip_ink, 10)
    )
    return svg(W, H, label, body)


ASSETS = {
    "banner": banner,
    "btn-havus": lambda t: button(t, "Try Havus", primary=True),
    "btn-support": lambda t: button(t, "Support Nyetok"),
}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name, build in ASSETS.items():
        for theme, tokens in THEMES.items():
            (OUT / f"{name}-{theme}.svg").write_text(build(tokens), encoding="utf-8")
    where = OUT.relative_to(Path.cwd()) if OUT.is_relative_to(Path.cwd()) else OUT
    print(f"wrote {len(ASSETS) * len(THEMES)} files to {where}")


if __name__ == "__main__":
    main()
