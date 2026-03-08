# Stable Diffusion Prompt Formulas

## Module 06: Code and Examples

---

## How to Use This Guide

Each formula provides a **positive prompt** and a **negative prompt** pair optimized for Stable Diffusion. Formulas are organized by use case with fill-in-the-blank templates and complete examples.

**Recommended Settings (unless noted otherwise):**
- Sampler: DPM++ 2M Karras
- Steps: 25-35
- CFG Scale: 7-9
- Resolution: 512x512 (SD 1.5) or 1024x1024 (SDXL)

---

## Formula 1: Photorealistic Portrait

### Template

```
POSITIVE:
RAW photo, (photorealistic:1.2), masterpiece, best quality,
portrait of [SUBJECT DESCRIPTION], [EXPRESSION], [CLOTHING],
[SETTING/BACKGROUND], shot on [CAMERA] with [LENS],
[APERTURE], [LIGHTING TYPE], [COLOR GRADING],
sharp focus, detailed skin texture, 8k uhd

NEGATIVE:
painting, illustration, drawing, cartoon, anime, 3d render,
bad anatomy, bad hands, bad fingers, blurry, low quality,
worst quality, watermark, text, signature, deformed face,
ugly, mutation, disfigured, extra limbs, poorly drawn face,
oversaturated, overexposed
```

### Example A: Corporate Headshot

```
POSITIVE:
RAW photo, (photorealistic:1.2), masterpiece, best quality,
portrait of a professional woman in her 30s, confident warm smile,
navy blazer over white blouse, clean gray gradient studio background,
shot on Canon EOS R5 with 85mm f/1.4 lens, f/2.0, Rembrandt lighting,
neutral color grading with warm tones, sharp focus, detailed skin
texture, 8k uhd, professional headshot

NEGATIVE:
painting, illustration, drawing, cartoon, anime, 3d render,
bad anatomy, bad hands, bad fingers, blurry, low quality,
worst quality, watermark, text, signature, deformed face,
ugly, mutation, disfigured, extra limbs, poorly drawn face,
oversaturated, overexposed, harsh shadows
```

### Example B: Environmental Portrait

```
POSITIVE:
RAW photo, (photorealistic:1.2), masterpiece, best quality,
environmental portrait of an elderly fisherman, weathered sun-tanned face,
deep wrinkles telling a lifetime of stories, warm genuine smile,
yellow rain jacket, standing on a weathered wooden dock,
fishing boats and harbor in background, shot on Nikon Z8 with 50mm f/1.8,
golden hour side lighting, warm earthy tones, shallow depth of field,
authentic and documentary, 8k uhd

NEGATIVE:
painting, illustration, drawing, cartoon, anime, 3d render,
bad anatomy, bad hands, bad fingers, blurry, low quality,
worst quality, watermark, text, signature, deformed face,
ugly, mutation, disfigured, extra limbs, poorly drawn face,
studio background, fake looking, plastic skin, airbrushed
```

### Example C: Fashion Portrait

```
POSITIVE:
RAW photo, (photorealistic:1.2), masterpiece, best quality,
fashion editorial portrait, model with bold red lipstick and slicked-back
hair, wearing oversized black blazer with gold brooch, dramatic
three-quarter pose, dark studio background with single rim light,
shot on Hasselblad X2D with 90mm lens, f/2.8, dramatic fashion lighting
with beauty dish, high contrast monochrome with selective red color,
Vogue magazine quality, sharp focus, 8k uhd

NEGATIVE:
bad anatomy, bad hands, bad fingers, blurry, low quality,
worst quality, watermark, text, signature, deformed face,
ugly, mutation, disfigured, extra limbs, poorly drawn face,
amateur, flat lighting, boring pose, cluttered background
```

---

## Formula 2: Landscape Photography

### Template

```
POSITIVE:
masterpiece, best quality, (breathtaking:1.2) [LANDSCAPE TYPE],
[SPECIFIC FEATURES], [SKY/WEATHER], [TIME OF DAY], [SEASON],
[ATMOSPHERE], [STYLE REFERENCE], (volumetric lighting:1.1),
[PERSPECTIVE/LENS], [COLOR PALETTE], ultra-detailed, sharp focus

NEGATIVE:
people, text, watermark, blurry, low quality, worst quality,
ugly, distorted, oversaturated, flat, boring, artifacts,
jpeg artifacts, cropped, deformed, bad proportions
```

### Example A: Mountain Vista

```
POSITIVE:
masterpiece, best quality, (breathtaking:1.3) alpine mountain landscape,
towering snow-capped granite peaks reflected in a crystal-clear glacial lake,
meadow of purple wildflowers in foreground, dramatic cumulus clouds with
golden hour light breaking through, late summer, epic and awe-inspiring,
National Geographic photography, (volumetric lighting:1.2), ultra-wide
angle 16mm lens perspective, rich greens, purples, and warm golden tones,
ultra-detailed, sharp focus, 8k resolution

NEGATIVE:
people, text, watermark, blurry, low quality, worst quality,
ugly, distorted, oversaturated, flat, boring, artifacts,
jpeg artifacts, cropped, deformed, bad proportions, buildings,
roads, man-made objects, hazy, washed out
```

### Example B: Moody Coastal

```
POSITIVE:
masterpiece, best quality, (dramatic:1.2) moody coastal landscape,
rugged sea cliffs with crashing waves, long exposure silky water,
overcast stormy sky with a single break in clouds letting light through,
winter, wild and untamed North Atlantic coast, fine art landscape
photography, (volumetric lighting:1.1), wide angle 24mm lens, muted
blue-gray palette with single beam of golden light, ultra-detailed,
sharp focus

NEGATIVE:
people, text, watermark, blurry, low quality, worst quality,
ugly, distorted, oversaturated, flat, boring, artifacts,
sunny, cheerful, tropical, calm water, clear sky
```

---

## Formula 3: Product Photography

### Template

```
POSITIVE:
(product photography:1.3), masterpiece, best quality,
[PRODUCT DESCRIPTION], [PRODUCT DETAILS], [SURFACE/BACKGROUND],
[LIGHTING SETUP], commercial photography, (clean:1.1), sharp focus,
studio shot, professional, 8k, high-end advertising

NEGATIVE:
text, watermark, logo, blurry, low quality, worst quality,
messy background, cluttered, amateur, dark, underexposed,
distorted, low resolution, jpeg artifacts, noisy
```

### Example A: Luxury Perfume

```
POSITIVE:
(product photography:1.3), masterpiece, best quality,
elegant glass perfume bottle with amber liquid, ornate gold cap with
crystal detail, on a dark marble surface, surrounded by fresh white
roses and scattered petals, (dramatic studio lighting:1.2) with soft
key light from above and warm accent light from behind, commercial
photography, (clean:1.1), sharp focus, studio shot, professional,
8k, high-end beauty advertising, luxury brand aesthetic

NEGATIVE:
text, watermark, logo, blurry, low quality, worst quality,
messy background, cluttered, amateur, dark, underexposed,
distorted, low resolution, jpeg artifacts, cheap looking,
plastic, fake flowers
```

### Example B: Tech Product

```
POSITIVE:
(product photography:1.3), masterpiece, best quality,
sleek wireless earbuds in charging case, matte black finish,
subtle LED indicator light, on a clean dark gray surface,
minimalist studio environment, edge lighting in subtle blue,
key light from above, Apple-style product photography,
(clean:1.2), razor sharp focus, 8k macro detail, premium tech
product advertising, modern minimal aesthetic

NEGATIVE:
text, watermark, logo, blurry, low quality, worst quality,
messy background, cluttered, fingerprints, dust, scratches,
reflections of photographer, amateur, distorted, noisy
```

---

## Formula 4: Anime/Illustration

### Template

```
POSITIVE:
masterpiece, best quality, (detailed anime illustration:1.2),
[CHARACTER DESCRIPTION], [EXPRESSION], [CLOTHING/OUTFIT],
[POSE/ACTION], [BACKGROUND/SETTING], [LIGHTING],
[COLOR PALETTE], [STYLE DETAILS], detailed face, beautiful eyes

NEGATIVE:
lowres, bad anatomy, bad hands, text, error, missing fingers,
extra digit, fewer digits, cropped, worst quality, low quality,
normal quality, jpeg artifacts, signature, watermark, username,
blurry, bad feet, poorly drawn face, extra limbs, mutated hands,
3d render, photorealistic, photograph
```

### Example A: Fantasy Character

```
POSITIVE:
masterpiece, best quality, (detailed anime illustration:1.2),
1girl, long flowing silver hair with blue highlights, piercing
ice-blue eyes, elegant pointed ears, wearing ornate dark blue and silver
mage robes with glowing rune patterns, casting a spell with swirling
ice crystals around raised hands, standing in an ancient frozen library,
bookshelves covered in frost, dramatic blue and purple lighting,
cool color palette with warm magical accents, highly detailed background,
detailed face, (beautiful detailed eyes:1.2), intricate clothing detail

NEGATIVE:
lowres, bad anatomy, bad hands, text, error, missing fingers,
extra digit, fewer digits, cropped, worst quality, low quality,
normal quality, jpeg artifacts, signature, watermark, username,
blurry, bad feet, poorly drawn face, extra limbs, mutated hands,
3d render, photorealistic, photograph, western style, ugly,
extra fingers, fused fingers
```

### Example B: Slice of Life

```
POSITIVE:
masterpiece, best quality, (detailed anime illustration:1.2),
1girl, short brown hair with hair clip, warm brown eyes, gentle smile,
wearing oversized cream sweater and plaid skirt, sitting at a cafe table
by the window, holding a warm cup of coffee, rainy day outside visible
through glass, warm indoor lighting, cozy autumn atmosphere, soft
watercolor-like background, warm orange and brown palette, detailed face,
(beautiful detailed eyes:1.2), Makoto Shinkai lighting style

NEGATIVE:
lowres, bad anatomy, bad hands, text, error, missing fingers,
extra digit, fewer digits, cropped, worst quality, low quality,
jpeg artifacts, signature, watermark, blurry, poorly drawn face,
extra limbs, mutated hands, 3d render, photorealistic, dark,
scary, horror, NSFW
```

---

## Formula 5: Concept Art

### Template

```
POSITIVE:
(concept art:1.3), masterpiece, best quality, [SCENE DESCRIPTION],
[ENVIRONMENTAL DETAILS], [ATMOSPHERE/MOOD], [LIGHTING],
[COLOR SCHEME], [REFERENCE ARTISTS], highly detailed,
digital painting, artstation, sharp focus

NEGATIVE:
photograph, photorealistic, 3d render, blurry, low quality,
worst quality, watermark, text, amateur, flat, boring,
uninspired, simple, generic, bad composition
```

### Example A: Fantasy Environment

```
POSITIVE:
(concept art:1.3), masterpiece, best quality, epic floating island
city above an ocean of clouds, cascading waterfalls falling from island
edges into the void below, crystal spires and ancient stone architecture,
airships docking at various levels, bioluminescent vegetation,
two moons visible in a twilight purple and gold sky, volumetric god rays,
warm golden light mixed with cool twilight blues, inspired by Ian McQue
and Craig Mullins, highly detailed, digital painting, artstation,
matte painting quality, epic scale

NEGATIVE:
photograph, photorealistic, 3d render, blurry, low quality,
worst quality, watermark, text, amateur, flat, boring,
simple, generic, bad composition, modern buildings, cars,
contemporary elements
```

### Example B: Sci-Fi Interior

```
POSITIVE:
(concept art:1.3), masterpiece, best quality, interior of a massive
spaceship bridge, holographic displays showing star maps and system
data, captain's chair overlooking a panoramic viewport showing a
nebula, sleek curved surfaces mixing organic and technological design,
crew stations with volumetric interfaces, dramatic blue and orange
lighting, lens flare from the nebula, inspired by Syd Mead and
Mass Effect, highly detailed, digital painting, cinematic composition,
widescreen aspect ratio

NEGATIVE:
photograph, photorealistic, blurry, low quality, worst quality,
watermark, text, amateur, flat, steampunk, fantasy, medieval,
cluttered, messy, bad perspective
```

---

## Formula 6: Vintage/Film Photography

### Template

```
POSITIVE:
RAW photo, (vintage photography:1.2), masterpiece, best quality,
[SUBJECT], [SETTING], [FILM STOCK] film aesthetic, [ERA] style,
[GRAIN/TEXTURE], [COLOR CHARACTERISTICS], authentic vintage feel,
nostalgic atmosphere, [COMPOSITION]

NEGATIVE:
modern, digital, clean, sharp, HDR, oversaturated, artificial,
plastic, bad anatomy, deformed, watermark, text, worst quality,
low quality, blurry
```

### Example A: 1970s Street Photography

```
POSITIVE:
RAW photo, (vintage photography:1.2), masterpiece, best quality,
candid street scene in New York City, people walking past a newsstand,
Kodachrome film aesthetic, 1970s style, visible film grain, warm
color shift with slightly faded shadows, authentic vintage feel,
nostalgic atmosphere, shot at eye level with a 35mm rangefinder camera,
slightly soft focus, natural street lighting

NEGATIVE:
modern clothing, smartphones, digital, clean, sharp, HDR,
oversaturated, artificial, plastic, bad anatomy, deformed,
watermark, text, worst quality, low quality, modern cars,
contemporary architecture
```

### Example B: Polaroid Style

```
POSITIVE:
RAW photo, (Polaroid photograph:1.3), masterpiece, best quality,
snapshot of a family picnic in a park, checkered blanket with food,
Polaroid SX-70 film aesthetic, 1980s style, characteristic Polaroid
color rendition with warm yellow-green shift, slightly overexposed
highlights, soft vintage focus, white Polaroid border frame,
nostalgic and personal, candid moment

NEGATIVE:
digital, sharp, HDR, modern, professional, studio, bad anatomy,
worst quality, low quality, blurry, deformed, watermark
```

---

## Formula 7: Digital Art / Fantasy Painting

### Template

```
POSITIVE:
masterpiece, best quality, (digital painting:1.2), [SUBJECT/SCENE],
[DETAILS], [LIGHTING AND ATMOSPHERE], [COLOR PALETTE],
[ART STYLE/INFLUENCES], highly detailed, artstation trending,
intricate details, sharp focus, vibrant

NEGATIVE:
photograph, photorealistic, 3d render, low quality, worst quality,
blurry, watermark, text, signature, bad anatomy, deformed,
amateur, flat colors, boring composition
```

### Example: Epic Battle Scene

```
POSITIVE:
masterpiece, best quality, (epic digital painting:1.3),
massive battle between a golden dragon and a dark knight on a
crumbling mountain fortress, dragon breathing fire that illuminates
the stormy sky, knight wielding a glowing enchanted sword, army
clashing below, (dramatic volumetric lighting:1.2), fire and storm
contrasting warm and cool tones, inspired by Frank Frazetta and
Donato Giancola, highly detailed, artstation trending, intricate armor
and scale details, sharp focus, cinematic composition, dynamic action

NEGATIVE:
photograph, photorealistic, low quality, worst quality,
blurry, watermark, text, signature, bad anatomy, deformed,
amateur, flat, boring, chibi, cute, cartoon, simple
```

---

## Formula 8: Architectural Visualization

### Template

```
POSITIVE:
(architectural visualization:1.2), masterpiece, best quality,
[BUILDING/SPACE DESCRIPTION], [MATERIALS], [SURROUNDINGS],
[LIGHTING CONDITIONS], [ATMOSPHERE], photorealistic rendering,
[CAMERA PERSPECTIVE], ultra-detailed, professional quality,
Architectural Digest style

NEGATIVE:
blurry, low quality, worst quality, watermark, text,
distorted perspective, impossible architecture, bad proportions,
unrealistic materials, cartoon, painting, dark, gloomy,
cluttered, messy, deformed
```

### Example: Modern Home

```
POSITIVE:
(architectural visualization:1.2), masterpiece, best quality,
stunning modern minimalist house with floor-to-ceiling glass walls,
clean white concrete and warm natural wood, cantilevered roofline,
infinity pool reflecting the mountain landscape, surrounded by native
desert vegetation, golden hour lighting creating warm shadows and
highlights, serene and luxurious atmosphere, photorealistic rendering,
wide-angle exterior view from the garden, ultra-detailed, professional
quality, Dwell magazine style

NEGATIVE:
blurry, low quality, worst quality, watermark, text,
distorted perspective, impossible architecture, bad proportions,
unrealistic materials, cartoon, painting, dark, gloomy,
cluttered, messy, deformed, ugly, cheap looking
```

---

## Formula 9: Food Photography

### Template

```
POSITIVE:
(food photography:1.3), masterpiece, best quality,
[DISH DESCRIPTION], [PLATING DETAILS], [SURFACE/TABLE],
[STYLING ELEMENTS], [LIGHTING], [ANGLE], [MOOD],
appetizing, professional food styling, sharp focus, detailed texture

NEGATIVE:
blurry, low quality, worst quality, watermark, text,
ugly, unappetizing, messy, dirty, bad lighting, artificial,
plastic food, oversaturated, underexposed, noisy, amateur
```

### Example: Fine Dining

```
POSITIVE:
(food photography:1.3), masterpiece, best quality,
beautifully plated pan-seared duck breast with cherry reduction,
microgreens and edible flowers, on a handmade black ceramic plate,
dark wood table with linen napkin, single glass of red wine,
(dramatic side lighting:1.2) from a window, moody dark food
photography, slightly overhead angle, warm and sophisticated mood,
appetizing, Michelin star presentation, professional food styling,
sharp focus, detailed texture on the seared skin

NEGATIVE:
blurry, low quality, worst quality, watermark, text,
ugly, unappetizing, messy, dirty, bad lighting, artificial,
plastic food, oversaturated, bright harsh lighting, fast food,
amateur plating, cluttered
```

---

## Formula 10: Children's Book Illustration

### Template

```
POSITIVE:
masterpiece, best quality, (children's book illustration:1.3),
[SCENE DESCRIPTION], [CHARACTERS], [SETTING], [ACTION],
[ART STYLE], warm and inviting, (detailed:1.1), storybook quality,
[COLOR PALETTE], charming and whimsical

NEGATIVE:
photorealistic, photograph, scary, dark, horror, violent,
bad anatomy, worst quality, low quality, blurry, text,
watermark, ugly, grotesque, disturbing, inappropriate for
children, realistic proportions
```

### Example: Forest Adventure

```
POSITIVE:
masterpiece, best quality, (children's book illustration:1.3),
a small fox cub wearing a tiny red scarf discovering a magical
door in the base of an enormous old oak tree, glowing warm light
from inside the door, friendly mushrooms with faces lining the path,
autumn forest with golden and red leaves, soft watercolor and
gouache art style, warm and inviting, (detailed:1.1), storybook
quality, warm autumnal palette of golds, reds, and forest greens,
charming and whimsical, Mary Blair meets Beatrix Potter

NEGATIVE:
photorealistic, photograph, scary, dark, horror, violent,
bad anatomy, worst quality, low quality, blurry, text,
watermark, ugly, grotesque, disturbing, realistic, anime,
manga, 3d render, sharp edges
```

---

## Quick Reference: Negative Prompt Presets

### Universal Negative (works with most prompts)
```
lowres, bad anatomy, bad hands, text, error, missing fingers,
extra digit, fewer digits, cropped, worst quality, low quality,
normal quality, jpeg artifacts, signature, watermark, username,
blurry, deformed, distorted, disfigured, mutation, ugly
```

### Photography Negative
```
illustration, painting, drawing, cartoon, anime, 3d render,
CGI, oversaturated, overexposed, underexposed, blown out,
crushed blacks, fake, artificial, plastic skin, airbrushed
```

### Illustration Negative
```
photorealistic, photograph, 3d render, CGI, text, watermark,
signature, frame, border, cropped, low quality, blurry,
inconsistent style, bad proportions
```

### Anime Negative
```
photorealistic, photograph, 3d, western, realistic, ugly,
extra fingers, mutated hands, poorly drawn face, lowres,
worst quality, low quality, blurry, watermark
```

---

## Tips for Better Results

1. **Quality tags first**: Always lead with "masterpiece, best quality"
2. **Weighted emphasis**: Use (important detail:1.3) for critical elements
3. **Negative prompts are essential**: They prevent common artifacts
4. **Match model to goal**: Use realistic models for photos, anime models for anime
5. **CFG 7-9**: Good balance for most prompts; lower for creativity, higher for precision
6. **Test and iterate**: Small prompt changes can produce big differences
7. **Order matters**: Earlier words in the prompt have slightly more influence
8. **Be specific**: "Canon 85mm f/1.4" beats "good camera"
9. **Combine formulas**: Mix elements from different formulas for unique results
10. **Check the model card**: Each fine-tuned model has recommended prompt styles

---

*Part of Module 06: AI for Visual, Audio, and Video Content Creation*
