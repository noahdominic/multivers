import fontforge

source = fontforge.open("Multivers-Semibold.sfdir")
target = fontforge.open("Multivers-Regular.sfdir")

print(target)
source_glyphs = list([glyph.glyphname for glyph in source.glyphs()])
target_glyphs = list([glyph.glyphname for glyph in target.glyphs()])

for glyphname in source_glyphs:
    if glyphname in target_glyphs:

        src_glyph = source[glyphname]
        tgt_glyph = target[glyphname]

        print("Processing", glyphname)

        width_adjust = (src_glyph.width - tgt_glyph.width)/2
        print("Width", tgt_glyph.width, "→", src_glyph.width, "with increment", width_adjust)
        tgt_glyph.left_side_bearing = int(tgt_glyph.left_side_bearing + width_adjust)
        tgt_glyph.right_side_bearing = int(tgt_glyph.right_side_bearing + width_adjust)

target.save("Multivers-Regular-temp.sfdir")
