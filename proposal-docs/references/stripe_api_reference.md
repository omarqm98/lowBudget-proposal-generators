# Stripe API Reference — Payment Links

## Overview

Creating a payment link requires three steps:
1. Create a **Product** (what the client is paying for)
2. Create a **Price** on that product (the amount)
3. Create a **Payment Link** using that price

## API Endpoints

### 1. Create Product
```
POST https://api.stripe.com/v1/products
Headers: Authorization: Bearer {STRIPE_SECRET_KEY}
Body (form-encoded):
  name=AI Lead Qualification — Acme Corp

Response: {"id": "prod_ABC123", "name": "AI Lead Qualification — Acme Corp", ...}
```

### 2. Create Price
```
POST https://api.stripe.com/v1/prices
Headers: Authorization: Bearer {STRIPE_SECRET_KEY}
Body (form-encoded):
  product=prod_ABC123
  unit_amount=175000          ← amount in cents ($1,750.00)
  currency=usd

Response: {"id": "price_XYZ789", "unit_amount": 175000, ...}
```

### 3. Create Payment Link
```
POST https://api.stripe.com/v1/payment_links
Headers: Authorization: Bearer {STRIPE_SECRET_KEY}
Body (form-encoded):
  line_items[0][price]=price_XYZ789
  line_items[0][quantity]=1

Response: {"id": "plink_...", "url": "https://buy.stripe.com/...", ...}
```

## Key Notes

- **Amount is in cents**: $1,500.00 = 150000 cents
- **Currency**: lowercase ISO code (usd, eur, pen, etc.)
- **Test mode**: use keys starting with `sk_test_` — no real charges
- **Live mode**: use keys starting with `sk_live_` — real money
- **Payment links are reusable** — the same link can be used by multiple customers
- **No expiration** by default — payment links stay active until manually deactivated
- **Stripe handles**: checkout page, payment processing, receipts, and confirmations
