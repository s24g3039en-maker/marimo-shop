import os

images = {
    "denim-pants.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F7F9FB" />
      <stop offset="100%" stop-color="#E8EEF5" />
    </linearGradient>
    <filter id="shadow2" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="10" flood-color="#1E3246" flood-opacity="0.12" />
    </filter>
  </defs>
  <rect width="400" height="400" rx="20" fill="url(#bgGrad2)" />
  <g filter="url(#shadow2)">
    <!-- Waistband -->
    <path d="M140 90 L260 90 L255 120 L145 120 Z" fill="#3D5A80" stroke="#293241" stroke-width="1.5" />
    <circle cx="200" cy="105" r="4" fill="#D4AF37" />
    <line x1="160" y1="90" x2="160" y2="120" stroke="#D4AF37" stroke-width="1.5" stroke-dasharray="3,2" />
    <line x1="240" y1="90" x2="240" y2="120" stroke="#D4AF37" stroke-width="1.5" stroke-dasharray="3,2" />
    <!-- Legs -->
    <path d="M145 120 L135 320 C135 325 175 325 175 320 L195 190 L205 190 L225 320 C225 325 265 325 265 320 L255 120 Z" fill="#4B6B94" stroke="#2B3A4E" stroke-width="2" />
    <!-- Stitching & Details -->
    <path d="M200 120 L200 170 C195 180 185 185 180 185" fill="none" stroke="#D4AF37" stroke-width="1.5" stroke-dasharray="4,2" />
    <path d="M150 135 C165 140 175 160 175 160" fill="none" stroke="#D4AF37" stroke-width="1.5" stroke-dasharray="3,2" />
    <path d="M250 135 C235 140 225 160 225 160" fill="none" stroke="#D4AF37" stroke-width="1.5" stroke-dasharray="3,2" />
    <!-- Cuffs roll -->
    <path d="M135 305 L175 305 L175 320 L135 320 Z" fill="#6B8CAE" stroke="#3D5A80" stroke-width="1" />
    <path d="M225 305 L265 305 L265 320 L225 320 Z" fill="#6B8CAE" stroke="#3D5A80" stroke-width="1" />
  </g>
</svg>''',

    "wool-knit.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FCF9F5" />
      <stop offset="100%" stop-color="#F2ECE4" />
    </linearGradient>
    <filter id="shadow3" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#5C4D3C" flood-opacity="0.12" />
    </filter>
  </defs>
  <rect width="400" height="400" rx="20" fill="url(#bgGrad3)" />
  <g filter="url(#shadow3)">
    <!-- Knit Body -->
    <path d="M140 110 L80 170 L105 195 L145 165 L145 305 C145 310 150 315 155 315 L245 315 C250 315 255 310 255 305 L255 165 L295 195 L320 170 L260 110 C240 125 220 130 200 130 C180 130 160 125 140 110 Z" fill="#C9ADA7" stroke="#A68A83" stroke-width="2" />
    <!-- Ribbed Collar -->
    <ellipse cx="200" cy="115" rx="35" ry="12" fill="#B3928B" stroke="#8E6E67" stroke-width="1.5" />
    <!-- Cable knit patterns -->
    <path d="M185 145 C180 160 190 175 185 190 C180 205 190 220 185 235 C180 250 190 265 185 280 C180 295 185 305 185 305" fill="none" stroke="#B3928B" stroke-width="2.5" stroke-linecap="round" />
    <path d="M215 145 C220 160 210 175 215 190 C220 205 210 220 215 235 C220 250 210 265 215 280 C220 295 215 305 215 305" fill="none" stroke="#B3928B" stroke-width="2.5" stroke-linecap="round" />
    <!-- Ribbed Hem & Cuffs -->
    <line x1="145" y1="305" x2="255" y2="305" stroke="#9A7B74" stroke-width="4" stroke-linecap="round" />
    <line x1="85" y1="175" x2="102" y2="192" stroke="#9A7B74" stroke-width="4" stroke-linecap="round" />
    <line x1="315" y1="175" x2="298" y2="192" stroke="#9A7B74" stroke-width="4" stroke-linecap="round" />
  </g>
</svg>''',

    "trench-coat.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FAF8F5" />
      <stop offset="100%" stop-color="#EFE9DE" />
    </linearGradient>
    <filter id="shadow4" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#3D382E" flood-opacity="0.12" />
    </filter>
  </defs>
  <rect width="400" height="400" rx="20" fill="url(#bgGrad4)" />
  <g filter="url(#shadow4)">
    <!-- Coat Body -->
    <path d="M150 90 L85 160 L110 185 L145 155 L135 340 L265 340 L255 155 L290 185 L315 160 L250 90 C235 105 218 110 200 110 C182 110 165 105 150 90 Z" fill="#D8C2A7" stroke="#BAA082" stroke-width="2" />
    <!-- Big Lapels -->
    <path d="M165 95 L140 150 L190 170 L200 130 Z" fill="#CBB296" stroke="#AA8F71" stroke-width="1.5" />
    <path d="M235 95 L260 150 L210 170 L200 130 Z" fill="#CBB296" stroke="#AA8F71" stroke-width="1.5" />
    <!-- Overlap & Double Breasted Buttons -->
    <line x1="185" y1="170" x2="175" y2="340" stroke="#B39879" stroke-width="1.5" />
    <circle cx="175" cy="185" r="4" fill="#5A4738" />
    <circle cx="215" cy="185" r="4" fill="#5A4738" />
    <circle cx="173" cy="225" r="4" fill="#5A4738" />
    <circle cx="217" cy="225" r="4" fill="#5A4738" />
    <circle cx="170" cy="265" r="4" fill="#5A4738" />
    <circle cx="219" cy="265" r="4" fill="#5A4738" />
    <!-- Belt with buckle -->
    <rect x="133" y="218" width="134" height="15" rx="3" fill="#BFA78C" stroke="#A1866B" stroke-width="1.5" />
    <rect x="190" y="214" width="20" height="23" rx="3" fill="none" stroke="#685544" stroke-width="2" />
    <line x1="200" y1="214" x2="200" y2="237" stroke="#685544" stroke-width="2" />
  </g>
</svg>''',

    "canvas-tote.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FBFBF9" />
      <stop offset="100%" stop-color="#EBEBE4" />
    </linearGradient>
    <filter id="shadow5" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#3B3F35" flood-opacity="0.12" />
    </filter>
  </defs>
  <rect width="400" height="400" rx="20" fill="url(#bgGrad5)" />
  <g filter="url(#shadow5)">
    <!-- Handles -->
    <path d="M165 170 L165 95 C165 75 235 75 235 95 L235 170" fill="none" stroke="#2D5A46" stroke-width="8" stroke-linecap="round" />
    <!-- Bag Body -->
    <path d="M125 160 L140 330 C141 336 146 340 152 340 L248 340 C254 340 259 336 260 330 L275 160 Z" fill="#F4EFE6" stroke="#DDD4C5" stroke-width="2" />
    <!-- Bottom Gusset / Accent -->
    <path d="M136 280 L140 330 C141 336 146 340 152 340 L248 340 C254 340 259 336 260 330 L264 280 Z" fill="#2D5A46" />
    <!-- Graphic on Bag -->
    <circle cx="200" cy="215" r="24" fill="#E8DED1" />
    <path d="M190 220 Q200 200 210 220" fill="none" stroke="#2D5A46" stroke-width="2.5" stroke-linecap="round" />
    <text x="200" y="255" font-family="'Helvetica Neue', sans-serif" font-size="9" font-weight="600" fill="#2D5A46" text-anchor="middle" letter-spacing="2">MARIMO BOTANICAL</text>
  </g>
</svg>''',

    "ceramic-mug.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F8FAF8" />
      <stop offset="100%" stop-color="#EAF0EA" />
    </linearGradient>
    <filter id="shadow6" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="#2D4A3E" flood-opacity="0.14" />
    </filter>
  </defs>
  <rect width="400" height="400" rx="20" fill="url(#bgGrad6)" />
  <g filter="url(#shadow6)">
    <!-- Mug Handle -->
    <path d="M245 160 C290 160 295 240 245 250" fill="none" stroke="#C49B74" stroke-width="14" stroke-linecap="round" />
    <!-- Mug Body -->
    <path d="M135 130 L145 280 C146 295 165 305 200 305 C235 305 254 295 255 280 L265 130 Z" fill="#EFE5D8" stroke="#D3C3B1" stroke-width="2" />
    <!-- Glaze Top Accent -->
    <path d="M135 130 C150 145 165 135 180 148 C195 155 210 142 225 150 C240 155 255 140 265 130 L265 170 C250 185 240 175 225 180 C210 185 195 170 180 182 C165 190 150 178 135 170 Z" fill="#406A56" />
    <!-- Rim opening -->
    <ellipse cx="200" cy="130" rx="65" ry="16" fill="#365848" stroke="#284437" stroke-width="2" />
    <ellipse cx="200" cy="133" rx="58" ry="12" fill="#5A3D28" />
    <!-- Steam -->
    <path d="M185 95 Q175 80 185 65" fill="none" stroke="#C4B8AB" stroke-width="2.5" stroke-linecap="round" opacity="0.6"/>
    <path d="M205 98 Q215 80 205 60" fill="none" stroke="#C4B8AB" stroke-width="2.5" stroke-linecap="round" opacity="0.6"/>
  </g>
</svg>''',

    "aroma-diffuser.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad7" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FBFBF9" />
      <stop offset="100%" stop-color="#EFF2EC" />
    </linearGradient>
    <filter id="shadow7" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="10" flood-color="#2D4A3E" flood-opacity="0.12" />
    </filter>
  </defs>
  <rect width="400" height="400" rx="20" fill="url(#bgGrad7)" />
  <g filter="url(#shadow7)">
    <!-- Reed Sticks -->
    <line x1="200" y1="210" x2="150" y2="70" stroke="#C7A77B" stroke-width="4" stroke-linecap="round" />
    <line x1="200" y1="210" x2="175" y2="55" stroke="#C7A77B" stroke-width="4" stroke-linecap="round" />
    <line x1="200" y1="210" x2="200" y2="50" stroke="#C7A77B" stroke-width="4" stroke-linecap="round" />
    <line x1="200" y1="210" x2="230" y2="60" stroke="#C7A77B" stroke-width="4" stroke-linecap="round" />
    <line x1="200" y1="210" x2="255" y2="75" stroke="#C7A77B" stroke-width="4" stroke-linecap="round" />
    <!-- Glass Bottle -->
    <rect x="185" y="195" width="30" height="20" rx="4" fill="#C4D7D1" stroke="#A0BCB3" stroke-width="2" />
    <path d="M150 215 C150 205 170 205 185 205 L215 205 C230 205 250 205 250 215 L255 315 C255 325 245 330 235 330 L165 330 C155 330 145 325 145 315 Z" fill="#DCEAE6" stroke="#9EBFB6" stroke-width="2" />
    <!-- Liquid inside -->
    <path d="M152 250 L248 250 L250 315 C250 322 242 325 235 325 L165 325 C158 325 150 322 150 315 Z" fill="#A8D0C3" opacity="0.6" />
    <!-- Minimalist Label -->
    <rect x="170" y="240" width="60" height="60" rx="2" fill="#FFFFFF" stroke="#E1E6E4" stroke-width="1" />
    <text x="200" y="263" font-family="'Helvetica Neue', sans-serif" font-size="7" font-weight="700" fill="#3D5348" text-anchor="middle" letter-spacing="1">FOREST</text>
    <text x="200" y="278" font-family="'Helvetica Neue', sans-serif" font-size="5.5" fill="#758A80" text-anchor="middle">Hinoki &amp; Herb</text>
  </g>
</svg>''',

    "leather-wallet.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad8" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FDFBF9" />
      <stop offset="100%" stop-color="#F4ECE1" />
    </linearGradient>
    <filter id="shadow8" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#4A3423" flood-opacity="0.14" />
    </filter>
  </defs>
  <rect width="400" height="400" rx="20" fill="url(#bgGrad8)" />
  <g filter="url(#shadow8)">
    <!-- Wallet Main Fold -->
    <rect x="110" y="140" width="180" height="130" rx="14" fill="#945D3B" stroke="#78482A" stroke-width="2" />
    <!-- Leather Texture Flap -->
    <path d="M110 140 L290 140 L290 205 C290 220 250 235 200 235 C150 235 110 220 110 205 Z" fill="#A86E48" stroke="#78482A" stroke-width="2" />
    <!-- Fine Stitching around Flap -->
    <path d="M115 145 L285 145 L285 202 C285 214 248 228 200 228 C152 228 115 214 115 202 Z" fill="none" stroke="#DFB98A" stroke-width="1.5" stroke-dasharray="4,2" />
    <!-- Brass Snap Button -->
    <circle cx="200" cy="205" r="7" fill="#E6C265" stroke="#B89230" stroke-width="1.5" />
    <circle cx="200" cy="205" r="3" fill="#D1AB43" />
    <!-- Side fold depth -->
    <path d="M290 160 L298 175 L290 190" fill="none" stroke="#683C21" stroke-width="2" />
  </g>
</svg>''',

    "linen-apron.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad9" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F8FAF7" />
      <stop offset="100%" stop-color="#ECF2EB" />
    </linearGradient>
    <filter id="shadow9" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="10" flood-color="#2D4A3E" flood-opacity="0.12" />
    </filter>
  </defs>
  <rect width="400" height="400" rx="20" fill="url(#bgGrad9)" />
  <g filter="url(#shadow9)">
    <!-- Neck Strap -->
    <path d="M175 105 C175 60 225 60 225 105" fill="none" stroke="#486856" stroke-width="4" stroke-linecap="round" />
    <!-- Waist Straps -->
    <path d="M130 195 L95 210" fill="none" stroke="#486856" stroke-width="4" stroke-linecap="round" />
    <path d="M270 195 L305 210" fill="none" stroke="#486856" stroke-width="4" stroke-linecap="round" />
    <!-- Apron Bib & Skirt -->
    <path d="M165 105 L235 105 L235 150 L270 185 L265 330 L135 330 L130 185 L165 150 Z" fill="#587E69" stroke="#3D5A4A" stroke-width="2" />
    <!-- Large Front Pockets -->
    <rect x="160" y="235" width="80" height="60" rx="4" fill="#4B6E5B" stroke="#375242" stroke-width="1.5" />
    <line x1="200" y1="235" x2="200" y2="295" stroke="#688F7A" stroke-width="1.5" stroke-dasharray="3,2" />
    <!-- Contrast Stitching on Hem -->
    <line x1="140" y1="322" x2="260" y2="322" stroke="#7FA591" stroke-width="1.5" stroke-dasharray="4,2" />
  </g>
</svg>''',

    "room-shoes.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad10" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FCF9F7" />
      <stop offset="100%" stop-color="#EFE8E2" />
    </linearGradient>
    <filter id="shadow10" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#4F443C" flood-opacity="0.12" />
    </filter>
  </defs>
  <rect width="400" height="400" rx="20" fill="url(#bgGrad10)" />
  <g filter="url(#shadow10)">
    <!-- Left Slipper -->
    <g transform="translate(-30, 0)">
      <ellipse cx="190" cy="270" rx="42" ry="18" fill="#B39E8E" stroke="#8E7867" stroke-width="1.5" />
      <path d="M152 265 C150 200 225 190 228 265 Z" fill="#D4C3B3" stroke="#9E8A7A" stroke-width="2" />
      <path d="M165 240 C175 220 205 220 215 240" fill="none" stroke="#BA9C87" stroke-width="2" />
    </g>
    <!-- Right Slipper -->
    <g transform="translate(50, -20)">
      <ellipse cx="190" cy="270" rx="42" ry="18" fill="#B39E8E" stroke="#8E7867" stroke-width="1.5" />
      <path d="M152 265 C150 200 225 190 228 265 Z" fill="#D4C3B3" stroke="#9E8A7A" stroke-width="2" />
      <path d="M165 240 C175 220 205 220 215 240" fill="none" stroke="#BA9C87" stroke-width="2" />
    </g>
  </g>
</svg>''',

    "pleated-skirt.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad11" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FBFBFD" />
      <stop offset="100%" stop-color="#EDEAF2" />
    </linearGradient>
    <filter id="shadow11" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#433B4E" flood-opacity="0.12" />
    </filter>
  </defs>
  <rect width="400" height="400" rx="20" fill="url(#bgGrad11)" />
  <g filter="url(#shadow11)">
    <!-- Waistband -->
    <rect x="155" y="110" width="90" height="16" rx="4" fill="#756D82" stroke="#564E63" stroke-width="1.5" />
    <!-- Skirt Body with pleats -->
    <path d="M155 126 L105 320 Q200 335 295 320 L245 126 Z" fill="#938B9E" stroke="#686073" stroke-width="2" />
    <!-- Pleat fold lines -->
    <line x1="170" y1="126" x2="135" y2="322" stroke="#756D82" stroke-width="1.5" />
    <line x1="185" y1="126" x2="168" y2="325" stroke="#A8A0B3" stroke-width="1.5" />
    <line x1="200" y1="126" x2="200" y2="326" stroke="#756D82" stroke-width="1.5" />
    <line x1="215" y1="126" x2="232" y2="325" stroke="#A8A0B3" stroke-width="1.5" />
    <line x1="230" y1="126" x2="265" y2="322" stroke="#756D82" stroke-width="1.5" />
  </g>
</svg>''',

    "silver-necklace.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad12" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F7FAF9" />
      <stop offset="100%" stop-color="#E5EFEA" />
    </linearGradient>
    <filter id="shadow12" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="10" flood-color="#2D4A3E" flood-opacity="0.12" />
    </filter>
  </defs>
  <rect width="400" height="400" rx="20" fill="url(#bgGrad12)" />
  <g filter="url(#shadow12)">
    <!-- Chain -->
    <path d="M140 100 Q200 270 200 270 Q200 270 260 100" fill="none" stroke="#BDC7C7" stroke-width="2.5" stroke-dasharray="3,2" />
    <!-- Pendant Rings -->
    <circle cx="200" cy="275" r="28" fill="none" stroke="#D1D9D9" stroke-width="4.5" />
    <circle cx="200" cy="275" r="16" fill="none" stroke="#A8B5B5" stroke-width="3" />
    <circle cx="200" cy="275" r="4" fill="#3D5A4D" />
  </g>
</svg>'''
}

out_dir = "/var/www/images"
for filename, content in images.items():
    with open(os.path.join(out_dir, filename), "w", encoding="utf-8") as f:
        f.write(content.strip())
print(f"Generated {len(images)} SVG images.")
