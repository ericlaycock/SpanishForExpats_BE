# spanish for expats - Master Reference Document

> **Last Updated**: March 2026  
> This document serves as the single source of truth for all design, development, and brand guidelines for the spanish for expats application.

---

## Table of Contents

1. [Application Overview](#application-overview)
2. [Brand Identity](#brand-identity)
3. [Logo](#logo)
4. [Color Palette](#color-palette)
5. [Typography](#typography)
6. [Design Tokens](#design-tokens)
7. [Component Guidelines](#component-guidelines)
8. [Tech Stack](#tech-stack)
9. [Project Structure](#project-structure)

---

## Application Overview

**spanish for expats** is a Spanish survival language learning application that teaches users through real-world conversational situations. The app focuses on immersive learning experiences with both text and voice conversation modes.

### Key Features
- Real-world situation-based learning
- Text and voice conversation modes
- Word tracking and progress monitoring
- Subscription-based access model
- Immersive learning scenarios with video content

---

## Brand Identity

### Mission
Master Spanish through real-world conversations

### Value Propositions
- Practice with real situations
- Learn vocabulary naturally
- Build confidence speaking

### Brand Personality
- **Approachable**: Friendly, encouraging learning environment
- **Modern**: Clean, contemporary design aesthetic
- **Engaging**: Interactive, immersive experiences
- **Trustworthy**: Professional, reliable language learning tool

---

## Logo

The brand logo is the **spanish for expats** mark (island icon + text on dark teal). It is used across the application for consistent branding.

- **Asset location**: `SpanishForExpats_FE/public/logo.png`
- **Served as**: `/logo.png` (Next.js public folder)
- **Usage**: Login page (left panel and mobile), Register page (left panel and mobile), Home page header
- **Alt text**: `spanish for expats`
- Use Next.js `Image` with appropriate width/height or object-contain to preserve aspect ratio.

---

## Color Palette

### Primary Colors

The application uses **dark teal** as its primary brand color (matching the logo background), with white for text and icons on teal.

#### Light Mode

| Color | HSL | Hex | Usage |
|-------|-----|-----|-------|
| **Primary (Brand Teal)** | `174 58% 38%` | `#28968C` | Main actions, buttons, links, branding panels, focus rings |
| **Primary Foreground** | `0 0% 100%` | `#FFFFFF` | Text on primary backgrounds |
| **Secondary** | `174 25% 90%` | Light teal tint | Secondary surfaces |
| **Secondary Foreground** | `174 58% 25%` | Dark teal | Text on secondary |

#### Brand Color
- **Primary teal**: `#28968C` — Use for branding panels (login/register), primary CTAs, links, and focus states.
- **On teal**: Always use white (or white/90) for text and icons.

### Semantic Colors

| Color | HSL | Hex | Usage |
|-------|-----|-----|-------|
| **Success** | `155 65% 45%` | `#10B981` | Success messages, completed states, positive feedback |
| **Warning** | `35 95% 55%` | `#F59E0B` | Warnings, caution states, important notices |
| **Destructive** | `0 75% 55%` | `#EF4444` | Errors, delete actions, destructive operations |
| **Accent** | `45 100% 95%` | `#FEF3C7` | Highlights, emphasis, callouts |

### Background Colors

| Color | HSL | Hex | Usage |
|-------|-----|-----|-------|
| **Background** | `174 30% 97%` | Light teal tint | Main application background |
| **Card** | `0 0% 100%` | `#FFFFFF` | Card backgrounds, modals, panels |
| **Muted** | `174 20% 93%` | Light teal tint | Subtle backgrounds, disabled states |

### Text Colors

| Color | HSL | Hex | Usage |
|-------|-----|-----|-------|
| **Foreground** | `220 20% 15%` | `#1E293B` | Primary text, headings |
| **Muted Foreground** | `220 15% 45%` | `#64748B` | Secondary text, descriptions |
| **Border** | `220 15% 88%` | `#E2E8F0` | Borders, dividers, input borders |

### Dark Mode

The application supports dark mode with adjusted color values:

| Color | HSL | Hex | Usage |
|-------|-----|-----|-------|
| **Background** | `220 15% 8%` | `#0F172A` | Dark mode background |
| **Foreground** | `220 10% 95%` | `#F1F5F9` | Dark mode text |
| **Primary** | `260 60% 60%` | `#8B5CF6` | Dark mode primary (purple variant) |
| **Card** | `220 15% 12%` | `#1E293B` | Dark mode cards |

### Color Usage Guidelines

1. **Primary Teal** (`#28968C`): Use for primary CTAs, branding panels, links, focus rings, and brand accents
2. **White on teal**: Use for all text and icons on teal backgrounds
3. **Backgrounds**: Use light teal tint (`from-teal-50 via-white to-teal-50`) for page backgrounds
4. **Semantic Colors**: Use consistently for their intended purposes (success, warning, error)
5. **Contrast**: Ensure WCAG AA compliance (4.5:1 for normal text, 3:1 for large text)

---

## Typography

### Font Family

**Primary Font**: **Montserrat** (Google Fonts)

The application uses Montserrat (weights 400, 600, 700) for a clean, modern sans-serif look that matches the logo. It is loaded via `next/font/google` and applied app-wide via the `--font-montserrat` CSS variable and Tailwind `font-sans`.

### Font Sizes

| Size | Usage | Example |
|------|-------|---------|
| `text-3xl` | Main headings, hero titles | "Welcome back" |
| `text-2xl` | Section headings | Page titles |
| `text-xl` | Subheadings, important text | Feature descriptions |
| `text-lg` | Body text, buttons | Primary content |
| `text-base` | Default body text | Paragraphs |
| `text-sm` | Secondary text, captions | Helper text, labels |
| `text-xs` | Fine print, metadata | Timestamps, small labels |

### Font Weights

| Weight | Usage |
|--------|-------|
| `font-bold` | Headings, important text |
| `font-semibold` | Buttons, emphasized text |
| `font-medium` | Labels, subheadings |
| `font-normal` | Body text (default) |

### Line Heights

- **Tight**: `leading-tight` - Headings
- **Normal**: `leading-normal` - Default body text
- **Relaxed**: `leading-relaxed` - Long-form content, descriptions

---

## Design Tokens

### Border Radius

| Token | Value | Usage |
|------|-------|-------|
| `--radius` | `1.25rem` (20px) | Default border radius for cards, buttons, inputs |
| `rounded-lg` | `var(--radius)` | Standard rounded corners |
| `rounded-xl` | Larger rounded corners | Cards, modals |
| `rounded-full` | `9999px` | Pills, badges, circular elements |
| `rounded-2xl` | Extra large | Hero sections, prominent cards |

### Spacing

The application uses Tailwind's default spacing scale (0.25rem increments):

| Scale | Value | Usage |
|------|-------|-------|
| `space-y-2` | `0.5rem` | Tight spacing between related items |
| `space-y-4` | `1rem` | Standard vertical spacing |
| `space-y-6` | `1.5rem` | Form field spacing |
| `space-y-8` | `2rem` | Section spacing |
| `gap-3` | `0.75rem` | Flex/grid item spacing |

### Shadows

| Shadow | Usage |
|--------|-------|
| `shadow-lg` | Cards, elevated elements |
| `shadow-xl` | Modals, prominent cards |
| `hover:shadow-xl` | Interactive elements on hover |

### Opacity

| Opacity | Usage |
|---------|-------|
| `opacity-20` | Subtle backgrounds, overlays |
| `opacity-50` | Disabled states |
| `opacity-60` | Secondary text in dark contexts |
| `opacity-80` | Semi-transparent elements |
| `opacity-90` | Slightly transparent overlays |

---

## Component Guidelines

### Buttons

**Primary Button**
- Background: `bg-[#28968C]` or `bg-brand`
- Hover: `hover:bg-teal-700`
- Text: White, semibold
- Padding: `px-8 py-6` (large) or `h-12` (standard)
- Border Radius: `rounded-lg` or `rounded-full`
- Shadow: `shadow-lg hover:shadow-xl`

**Secondary Button**
- Background: `bg-secondary` or `bg-gray-100`
- Text: `text-gray-900` or `text-secondary-foreground`
- Similar padding and radius as primary

### Cards

- Background: `bg-white` (light) or `bg-card` (dark)
- Border: `border border-gray-100` or `border-border`
- Border Radius: `rounded-2xl`
- Padding: `p-8` (standard) or `p-6` (compact)
- Shadow: `shadow-xl`

### Input Fields

- Background: `bg-white` or `bg-input`
- Border: `border-gray-300` or `border-input`
- Focus: `focus:border-teal-500 focus:ring-teal-500`
- Border Radius: `rounded-lg`
- Padding: `pl-10` (with icons) or `px-4 py-3`
- Height: `h-12` (standard)

### Login / Register Pages

- Single centered column layout (no split panel) — mobile-first
- White/off-white background (`bg-gray-50`)
- Logo displayed on light background where its built-in teal gradient is the visual anchor
- Form in white card below logo
- Same layout on mobile and desktop

**Logo usage note**: `logo.png` has a teal gradient baked into the PNG. Always display it on white or off-white backgrounds — never on teal, as it creates a visible rectangular clash.

### Page Backgrounds

**Page Background Gradient**
```css
bg-gradient-to-br from-teal-50 via-white to-teal-50
```
Used for: Page backgrounds, subtle depth

---

## Tech Stack

### Frontend
- **Framework**: Next.js 16.1.6
- **Language**: TypeScript
- **Styling**: Tailwind CSS 3.4.17
- **UI Components**: shadcn/ui (Radix UI primitives)
- **State Management**: React Hooks
- **Icons**: Lucide React
- **Fonts**: Montserrat (Google Fonts, via next/font)

### Backend
- **Framework**: FastAPI (Python 3.11)
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Migrations**: Alembic
- **Authentication**: JWT (python-jose)
- **AI Integration**: OpenAI API (GPT-4.1-mini, Whisper STT, TTS)

### Infrastructure
- **Deployment**: Railway
- **Containerization**: Docker
- **Version Control**: Git

---

## Project Structure

```
spanishforexpats/
├── SpanishForExpats_FE/          # Next.js frontend application
│   ├── app/              # Next.js app router pages
│   ├── components/       # React components
│   ├── lib/              # Utilities and API client
│   ├── styles/           # Global styles
│   └── public/           # Static assets (logo.png = brand logo)
├── SpanishForExpats_BE/          # FastAPI backend application
│   ├── app/              # Application code
│   │   ├── api/v1/       # API endpoints
│   │   ├── services/     # Business logic
│   │   ├── models.py     # Database models
│   │   └── schemas.py    # Pydantic schemas
│   └── migrations/       # Database migrations
└── assets/              # Shared assets (videos, etc.)
```

---

## Design Principles

1. **Clarity First**: Prioritize clear communication and intuitive interfaces
2. **Consistent Patterns**: Use established patterns throughout the application
3. **Accessibility**: Ensure WCAG AA compliance for all users
4. **Performance**: Optimize for fast load times and smooth interactions
5. **Responsive**: Design for all screen sizes (mobile-first approach)
6. **Immersive**: Create engaging, focused learning experiences

---

## Quick Reference

### Most Used Colors
- **Primary Teal**: `#28968C` (brand)
- **Background**: Light teal tint (teal-50)
- **Text**: `#1E293B` (slate-800)

### Most Used Classes
- `bg-[#28968C]` or `bg-brand` - Primary buttons and brand panels
- `hover:bg-teal-700` - Primary button hover
- `rounded-2xl` - Card corners
- `shadow-xl` - Card shadows
- `text-gray-600` - Secondary text
- `h-12` - Standard input/button height

---

## Maintenance

This document should be updated whenever:
- New colors are added to the palette
- Typography standards change
- New design patterns are established
- Component guidelines are updated
- Tech stack changes

**Maintainer**: Development Team  
**Review Frequency**: Quarterly or as needed

---

*This document is the authoritative source for all design and development decisions. When in doubt, refer to this document.*


