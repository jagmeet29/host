# Complete Markdown Syntax Reference

This document provides a comprehensive guide to all markdown syntax and features supported by the File Browser application.

## 🎯 Quick Reference

| Feature | Syntax | Description |
|---------|--------|-------------|
| **Basic Callouts** | `>[!Note]` | Info, Warning, Tip, etc. |
| **Q&A Format** | `>[!question]` | Interactive Q&A blocks |
| **Wiki Links** | `[[filename]]` | Internal file linking |
| **Image Embeds** | `![[image.png]]` | Smart image embedding |
| **Math** | `$equation$` | LaTeX math rendering |
| **Themes** | 🌙/☀️ button | Dark/Light mode toggle |

---

## 📝 General Callouts

Create beautiful, color-coded callouts for different types of content:

### Available Callout Types

| Type | Icon | Syntax | Use Case |
|------|------|--------|----------|
| **Note** | 📝 | `>[!Note]` | General information |
| **Warning** | ⚠️ | `>[!Warning]` | Important warnings |
| **Tip** | 💡 | `>[!Tip]` | Helpful suggestions |
| **Info** | ℹ️ | `>[!Info]` | Additional information |
| **Success** | ✅ | `>[!Success]` | Positive outcomes |
| **Error** | ❌ | `>[!Error]` | Error messages |
| **Question** | ❓ | `>[!Question]` | Questions to consider |
| **Example** | 📋 | `>[!Example]` | Code or concept examples |
| **Important** | 🔥 | `>[!Important]` | Critical information |

### Examples

>[!Note]
>XOR and XNOR gates are self dual [[DE/Boolean/duality.md|What is Dual ?]]

>[!Warning]
>Be careful when handling electrical components. Always check voltage levels before connecting circuits.

>[!Tip]
>Use De Morgan's laws to simplify complex Boolean expressions more efficiently.

>[!Important]
>Always double-check your circuit connections before applying power to prevent damage to components.

### Multi-line Callouts

>[!Example]
>A simple AND gate truth table:
>- 0 AND 0 = 0
>- 0 AND 1 = 0  
>- 1 AND 0 = 0
>- 1 AND 1 = 1
>
>You can include **formatting**, *emphasis*, and even [[links]] inside callouts!

---

## ❓ Interactive Q&A Format

Create collapsible question-answer pairs with special syntax:

### Syntax
```markdown
>[!question] Your question here?
>> [!success]- Answer
>> Your answer content here
>> Can span multiple lines
>> Supports **markdown** formatting
```

### Example

>[!question] What is Boolean algebra?
>> [!success]- Answer
>> Boolean algebra is a branch of mathematics that deals with operations on logical values.
>> It uses binary variables that can only have two possible values: true (1) or false (0).
>> 
>> The basic operations in Boolean algebra are:
>> - AND (∧)
>> - OR (∨)  
>> - NOT (¬)

>[!question] How do you simplify Boolean expressions?
>> [!success]- Answer
>> You can simplify Boolean expressions using:
>> 1. **Boolean Laws** (Identity, Null, Idempotent, etc.)
>> 2. **De Morgan's Laws**
>> 3. **Karnaugh Maps** for visual simplification
>> 4. **Algebraic manipulation**

---

## 🔗 Wiki-Style Linking

Link to other files seamlessly using wiki-style syntax:

### Link Types

| Syntax | Description | Example |
|--------|-------------|---------|
| `[[filename]]` | Basic link | `[[duality]]` |
| `[[filename\|Display Text]]` | Custom text | `[[duality\|What is Dual?]]` |
| `[[path/file.md]]` | Full path | `[[DE/Boolean/duality.md]]` |
| `[[path/file\|Text]]` | Path + custom text | `[[DE/Boolean/duality.md\|Duality Concept]]` |

### Examples

- Basic link: [[syntax-examples]]
- With custom text: [[syntax-examples|Syntax Guide]]
- Full path: [[DE/Boolean/duality.md]]
- Path with custom text: [[DE/Boolean/duality.md|Learn about Duality]]

### Auto-Extension
- Links without extensions automatically get `.md` added
- Links are resolved relative to the current file's directory
- System searches multiple common paths if file not found locally

---

## 🖼️ Image Embedding

Embed images using wiki-style syntax with smart path resolution:

### Syntax
```markdown
![[image.png]]
![[subfolder/image.jpg]]
```

### Smart Path Resolution
The system automatically searches for images in:
1. Current file's directory
2. `img/` subdirectory
3. `images/` subdirectory
4. Parent directory paths
5. Global `../notesob/img/` directory

### Supported Formats
- `.png`, `.jpg`, `.jpeg`
- `.gif`, `.svg`, `.webp`, `.bmp`

### Examples
```markdown
![[logic-gate.png]]
![[Boolean/img/truth-table.jpg]]
```

### Fallback Display
If image not found, shows helpful error message with searched paths.

---

## 🧮 LaTeX Math Support

Render mathematical expressions using MathJax:

### Inline Math
Use single dollar signs for inline equations:
```markdown
The Boolean function $F = A \cdot B + C$ represents...
```
Result: The Boolean function $F = A \cdot B + C$ represents...

### Block Math
Use double dollar signs for centered block equations:
```markdown
$$F(A,B,C) = \sum m(1,3,5,7)$$
```
Result:
$$F(A,B,C) = \sum m(1,3,5,7)$$

### Alternative Syntax
Also supports LaTeX delimiters:
- Inline: `\(...\)`
- Block: `\[...\]`

### Common Symbols
| Symbol | LaTeX | Symbol | LaTeX |
|--------|-------|--------|-------|
| ∧ | `\land` or `\cdot` | ∨ | `\lor` or `+` |
| ¬ | `\neg` or `\overline{}` | ⊕ | `\oplus` |
| ∑ | `\sum` | ∏ | `\prod` |

---

## 📊 Tables

Standard markdown tables with auto-scrolling wrapper:

### Basic Table
```markdown
| Gate | Input A | Input B | Output |
|------|---------|---------|---------|
| AND  | 0       | 0       | 0       |
| AND  | 0       | 1       | 0       |
| AND  | 1       | 0       | 0       |
| AND  | 1       | 1       | 1       |
```

### Table Features
- Auto-wrapping for horizontal scrolling
- Responsive design
- Theme-aware styling
- Support for formatting within cells

---

## 💻 Code Blocks

Syntax highlighted code blocks:

### Verilog Example
```verilog
module and_gate (
    input a,
    input b,
    output y
);
    assign y = a & b;
endmodule
```

### Python Example
```python
def boolean_and(a, b):
    return a and b

# Truth table generation
for a in [0, 1]:
    for b in [0, 1]:
        print(f"{a} AND {b} = {boolean_and(a, b)}")
```

### Inline Code
Use backticks for `inline code` within sentences.

---

## 📝 Standard Markdown

All standard markdown features are supported:

### Headers
```markdown
# Header 1
## Header 2
### Header 3
#### Header 4
##### Header 5
###### Header 6
```

### Text Formatting
- **Bold text** using `**text**`
- *Italic text* using `*text*`
- ***Bold and italic*** using `***text***`
- ~~Strikethrough~~ using `~~text~~`

### Lists

#### Unordered Lists
- Item 1
- Item 2
  - Nested item
  - Another nested item
- Item 3

#### Ordered Lists
1. First item
2. Second item
   1. Nested numbered item
   2. Another nested item
3. Third item

### Blockquotes
> This is a blockquote
> It can span multiple lines
> > And can be nested

### Horizontal Rules
Use three dashes for horizontal rules:
```markdown
---
```
---

### Links
- External: [GitHub](https://github.com)
- Email: [contact@example.com](mailto:contact@example.com)
- Reference style: [link text][reference]

[reference]: https://example.com

---

## 🎨 Theme System

### Theme Toggle
- Click the 🌙/☀️ button in the top-right corner
- Automatically saves preference to localStorage
- Affects all callouts, code blocks, and UI elements

### Theme Features
- **Dark Mode**: Default black background with orange accents
- **Light Mode**: Clean white background with blue accents
- **Consistent Colors**: All callouts and elements adapt to theme
- **Persistent**: Theme choice remembered across sessions

---

## 🗂️ File Browser Features

### Navigation
- **Compact View**: Toggle with 📋 button for condensed file list
- **Refresh**: 🔄 button to reload file listings
- **Home**: 🏠 button to return to main directory
- **Breadcrumb**: Shows current path location

### File Discovery
- Automatic directory listing generation
- Searches for markdown files (`.md`)
- Folder navigation with back buttons
- File caching for improved performance

### State Management
- Remembers last viewed file
- Restores navigation state on page load
- localStorage integration for persistence

---

## ⚙️ Processing Order

The system processes content in this order:

1. **Wiki Links** (`[[...]]`) - Converts to clickable links
2. **Q&A Format** (`>[!question]`) - Creates interactive blocks  
3. **General Callouts** (`>[!note]`) - Renders colored callouts
4. **Standard Markdown** - Processes headers, lists, etc.
5. **Math Rendering** - Renders LaTeX expressions
6. **Table Wrapping** - Adds scrollable containers
7. **JavaScript Initialization** - Activates interactive elements

---

## 🔧 Advanced Features

### File Path Resolution
- Relative paths resolved from current file location
- Smart searching across common directories
- Automatic `.md` extension addition
- Fallback error messages with search paths

### Content Caching
- File listings cached for performance
- Automatic cache invalidation
- Browser localStorage integration

### Responsive Design
- Mobile-friendly layout
- Touch-friendly buttons
- Adaptive spacing and sizing
- Horizontal scroll prevention

---

## 📖 Usage Tips

### Best Practices
1. **Use descriptive link text**: `[[file|Good Description]]` instead of `[[file]]`
2. **Organize with callouts**: Use appropriate callout types for content
3. **Structure with headers**: Use consistent header hierarchy
4. **Include alt text**: Always provide meaningful image descriptions
5. **Test math**: Preview LaTeX equations before finalizing

### Performance Tips
1. **Image optimization**: Use compressed images for faster loading
2. **File organization**: Keep related files in same directories
3. **Link validation**: Regularly check that internal links work
4. **Cache refresh**: Use refresh button if files don't appear

### Troubleshooting
- **Links not working**: Check file paths and extensions
- **Images not showing**: Verify image exists in expected location
- **Math not rendering**: Check LaTeX syntax and delimiters
- **Theme issues**: Try toggling theme or refreshing page

---

*This reference covers all supported syntax and features. The system is continuously being enhanced with new capabilities.*
