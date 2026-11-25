---
name: ai-image-generation
description: Generate and edit AI images via the inference.sh `belt` CLI. Use when Codex is asked for AI art, image generation, text-to-image, image-to-image, inpainting, image editing, upscaling, product mockups, concept art, social media graphics, marketing visuals, illustrations, or when prompts mention FLUX, GPT image, OpenAI image, Gemini image, Grok image, Seedream, Reve, stable diffusion, Midjourney alternative, DALL-E alternative, text2img, or image generator.
---

# AI Image Generation

Use this skill to generate or edit images through the inference.sh `belt` CLI when it is available. Model availability changes, so verify current app IDs with `belt app store --category image` before relying on a specific model.

If `belt` is not installed or the user is not logged in, explain the blocker and ask before installing or authenticating. Do not invent generated files; only report outputs that were actually created or returned by the CLI.

## Quick Checks

Check CLI availability:

```bash
belt --help
```

Log in when needed:

```bash
belt login
```

Browse image apps:

```bash
belt app store --category image
```

## Common Models

Use the current app store output as the source of truth. Known app IDs from the provided skill text include:

| Model | App ID | Best For |
| --- | --- | --- |
| GPT-Image-2 | `openai/gpt-image-2` | Text-to-image, editing, inpainting |
| FLUX Dev LoRA | `falai/flux-dev-lora` | High-quality images with custom styles |
| FLUX.2 Klein LoRA | `falai/flux-2-klein-lora` | Fast LoRA-supported generation |
| P-Image | `pruna/p-image` | Fast economical generation |
| P-Image-LoRA | `pruna/p-image-lora` | Fast generation with preset LoRA styles |
| P-Image-Edit | `pruna/p-image-edit` | Fast image editing |
| Gemini 3 Pro Image | `google/gemini-3-pro-image-preview` | Google image generation |
| Gemini 2.5 Flash Image | `google/gemini-2-5-flash-image` | Fast Google image generation |
| Grok Imagine | `xai/grok-imagine-image` | Multiple aspect ratios |
| Seedream 4.5 | `bytedance/seedream-4-5` | 2K-4K cinematic quality |
| Seedream 4.0 | `bytedance/seedream-4-0` | 2K-4K quality |
| Seedream 3.0 | `bytedance/seedream-3-0-t2i` | Text rendering |
| Reve | `falai/reve` | Natural-language editing and text rendering |
| ImagineArt 1.5 Pro | `falai/imagine-art-1-5-pro-preview` | Ultra-high-fidelity 4K |
| FLUX Klein 4B | `pruna/flux-klein-4b` | Low-cost generation |
| Topaz Upscaler | `falai/topaz-image-upscaler` | Professional upscaling |

## Usage Patterns

Generate with FLUX:

```bash
belt app run falai/flux-dev-lora --input '{"prompt": "professional product photo of a coffee mug, studio lighting"}'
```

Generate with GPT-Image-2:

```bash
belt app run openai/gpt-image-2 --input '{
  "prompt": "professional product photo of sneakers, studio lighting",
  "quality": "high"
}'
```

Edit with GPT-Image-2:

```bash
belt app run openai/gpt-image-2 --input '{
  "prompt": "change the background to a beach at sunset",
  "images": ["https://your-image.jpg"]
}'
```

Generate with Grok Imagine:

```bash
belt app run xai/grok-imagine-image --input '{
  "prompt": "cyberpunk city at night",
  "aspect_ratio": "16:9"
}'
```

Generate with Reve for text rendering:

```bash
belt app run falai/reve --input '{
  "prompt": "A poster that says HELLO WORLD in bold letters"
}'
```

Upscale:

```bash
belt app run falai/topaz-image-upscaler --input '{"image_url": "https://..."}'
```

Stitch images:

```bash
belt app run infsh/stitch-images --input '{
  "images": ["https://img1.jpg", "https://img2.jpg"],
  "direction": "horizontal"
}'
```

## Workflow

1. Clarify the target format, aspect ratio, style, subject, and output use when the prompt is underspecified.
2. Choose the model by task: generation, editing, inpainting, text rendering, LoRA style, or upscaling.
3. Run the `belt` command with structured JSON input.
4. Save or reference the returned output exactly as provided by the CLI.
5. Verify the generated image visually when local files are produced.

## Related Installation Notes

The provided source text suggests installing the belt CLI skill with:

```bash
npx skills add belt-sh/cli
```

Only run install commands after user approval, because they require network access and change the local environment.
