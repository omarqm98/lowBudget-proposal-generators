# Carbone.io API Reference

## Tag Syntax

Simple replacement:
```
{d.fieldName}              → replaces with the value of fieldName
{d.client.firstName}       → nested object access
```

## Array Loops (Dynamic Table Rows)

Place tags inside a table row — Carbone auto-repeats the row for each item in the array:
```
{d.lineItems[i].name}     → loops over lineItems array
{d.lineItems[i].price}    → each field in the same row
{d.lineItems[i+1].name}   → marks where the next row starts (optional, needed for complex layouts)
```

The `[i]` marker tells Carbone this is a repeating row. No additional configuration needed.

## Formatters

Number formatting:
```
{d.price:formatN(2)}                    → 1500.00
{d.price:formatC('en-US','USD')}        → $1,500.00
{d.price:formatC('es-PE','PEN')}        → S/ 1,500.00
```

Date formatting:
```
{d.date:formatD('YYYY-MM-DD')}          → 2025-03-15
{d.date:formatD('MMMM D, YYYY')}       → March 15, 2025
```

Conditional display:
```
{d.field:ifEQ('value'):show()}          → shows content only if field equals 'value'
{d.field:ifNE(''):show()}               → shows content only if field is not empty
```

## REST API Endpoints

### Upload Template
```
POST https://api.carbone.io/template
Headers: Authorization: Bearer {API_KEY}
Body: multipart/form-data with file field "template"

Response: {"success": true, "data": {"templateId": "abc123..."}}
```

### Render Document
```
POST https://api.carbone.io/render/{templateId}
Headers:
  Authorization: Bearer {API_KEY}
  Content-Type: application/json
Body: {"data": {...}, "convertTo": "pdf"}

Response: {"success": true, "data": {"renderId": "xyz789..."}}
```

### Download Rendered Document
```
GET https://api.carbone.io/render/{renderId}
Headers: Authorization: Bearer {API_KEY}

Response: binary file content (PDF, DOCX, etc.)
```

## Important Notes

- **Template IDs are persistent** — upload once, reuse many times with different data
- **Rendered documents expire in 1 hour** and auto-delete after first download
- **Free tier**: 100 documents/month, 100 templates, 1 parallel render
- **Template format**: .docx (Word) recommended for best results with tables and styling
- **Output formats**: pdf, docx, xlsx, pptx, html, odt, ods, odp, jpg, png
- **Nested objects**: use dot notation `{d.client.firstName}`
- **Array loops in tables**: just put `{d.array[i].field}` in a table cell — Carbone handles row repetition
