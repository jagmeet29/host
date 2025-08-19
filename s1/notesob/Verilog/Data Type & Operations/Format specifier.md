The `$display`, `$write`, and `$sprintf` functions utilize format specifiers to control the output of variables.

|Format Specifier|Type Example|Description/Output Example|
|---|---|---|
|`%b`|`int`, `reg`, `bit`|Binary (e.g., `$display("%b", a);` → 1010)|
|`%d`|`int`, `shortint`|Decimal (e.g., `$display("%d", a);` → 42)|
|`%h`|`int`, `logic`|Hexadecimal (e.g., `$display("%h", a);` → A)|
|`%o`|`int`, `reg`|Octal (e.g., `$display("%o", a);` → 12)|
|`%c`|`char` (SV)|Character (e.g., `$display("%c", 'A');` → A)|
|`%s`|`string` (SV)|String (e.g., `$display("%s", "Hello");`)|
|`%t`|`$time`|Time (e.g., `$display("%t", $time);`)|
|`%v`|Any type|Variable value (no format conversion)|

**Note:**

- **Integer types** (`int`, `shortint`, `longint`, `byte`, `integer`) are commonly used with `%d`, `%h`, `%b`, and `%o`.
- `%v` displays the value as-is, without base conversion.
- `%0d`, `%0h`, etc., suppress leading zeros.
