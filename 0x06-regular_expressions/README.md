# 0x06. Regular expressions

## Description
This project introduces regular expressions (regex) and their application in text processing and pattern matching. You'll learn how to construct and use regular expressions to search, match, and manipulate text data efficiently using Ruby's Oniguruma regex library.

## Learning Objectives
By the end of this project, you should be able to explain:

- What is a regular expression
- What are the different types of regular expression engines
- How to build a regular expression
- How to use basic regex patterns and metacharacters
- How to use character classes and quantifiers
- How to use anchors and boundaries
- How to use groups and backreferences
- How to apply regular expressions in Ruby
- Common regex patterns for validation and text processing

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted on Ubuntu 20.04 LTS
- All files should end with a new line
- A `README.md` file at the root of the project folder is mandatory
- All Bash script files must be executable
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining what the script does

### Ruby Scripts
- All Ruby files will be interpreted/compiled on Ubuntu 20.04 LTS using ruby (version 2.7.0)
- The first line of all Ruby files should be exactly `#!/usr/bin/env ruby`
- All regex must work with the Oniguruma library (Ruby's default regex engine)

### Regex Requirements
- You can only use the `=~` operator for regex matching in Ruby
- Your regex patterns should be simple and efficient
- Test your regex patterns thoroughly with various inputs

## Concepts Covered

### What is a Regular Expression?
A regular expression (regex) is a sequence of characters that defines a search pattern. It's used for:
- Pattern matching in strings
- Text validation (email, phone numbers, etc.)
- Text extraction and replacement
- Data parsing and processing

### Regex Engines
- **PCRE (Perl Compatible Regular Expressions)**: Used in PHP, JavaScript, Python
- **POSIX**: Standard Unix regex
- **Oniguruma**: Ruby's default regex engine
- **RE2**: Google's regex engine (used in Go)

### Basic Regex Syntax

#### Literal Characters
```regex
hello           # Matches exactly "hello"
123             # Matches exactly "123"
```

#### Metacharacters
- `.` - Matches any single character (except newline)
- `^` - Matches start of string/line
- `$` - Matches end of string/line
- `*` - Matches 0 or more of preceding character
- `+` - Matches 1 or more of preceding character
- `?` - Matches 0 or 1 of preceding character
- `|` - Alternation (OR)
- `\` - Escape character

#### Character Classes
```regex
[abc]           # Matches 'a', 'b', or 'c'
[a-z]           # Matches any lowercase letter
[A-Z]           # Matches any uppercase letter
[0-9]           # Matches any digit
[^abc]          # Matches anything except 'a', 'b', or 'c'
```

#### Predefined Character Classes
```regex
\d              # Matches any digit [0-9]
\D              # Matches any non-digit
\w              # Matches word characters [a-zA-Z0-9_]
\W              # Matches non-word characters
\s              # Matches whitespace characters
\S              # Matches non-whitespace characters
```

#### Quantifiers
```regex
{n}             # Exactly n times
{n,}            # n or more times
{n,m}           # Between n and m times
*               # 0 or more times (same as {0,})
+               # 1 or more times (same as {1,})
?               # 0 or 1 time (same as {0,1})
```

#### Anchors and Boundaries
```regex
^               # Start of string/line
$               # End of string/line
\b              # Word boundary
\B              # Non-word boundary
\A              # Start of string
\z              # End of string
```

#### Groups and Capturing
```regex
(pattern)       # Capturing group
(?:pattern)     # Non-capturing group
\1, \2, etc.    # Backreferences to captured groups
```

## Common Regex Patterns

### Email Validation
```regex
^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
```

### Phone Number (US Format)
```regex
^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$
```

### URL Validation
```regex
^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)$
```

### IPv4 Address
```regex
^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$
```

### Password Strength (8+ chars, uppercase, lowercase, digit)
```regex
^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d@$!%*?&]{8,}$
```

## Ruby Regex Usage

### Basic Matching
```ruby
#!/usr/bin/env ruby
# Basic regex matching in Ruby

string = "Hello, World!"
pattern = /[Hh]ello/

if string =~ pattern
    puts "Match found!"
else
    puts "No match found"
end
```

### Extracting Matches
```ruby
#!/usr/bin/env ruby
# Extract phone numbers from text

text = "Call me at 555-123-4567 or 555.987.6543"
phone_pattern = /\d{3}[-.]?\d{3}[-.]?\d{4}/

phones = text.scan(phone_pattern)
phones.each { |phone| puts phone }
```

### Using Match Groups
```ruby
#!/usr/bin/env ruby
# Extract parts of a date

date_string = "2023-12-25"
date_pattern = /(\d{4})-(\d{2})-(\d{2})/

if match = date_string.match(date_pattern)
    year, month, day = match.captures
    puts "Year: #{year}, Month: #{month}, Day: #{day}"
end
```

## Examples

### Simple Pattern Matching
```ruby
#!/usr/bin/env ruby
# Match words starting with capital letter
puts ARGV[0].scan(/\b[A-Z]\w*/).join(",")
```

### Email Extraction
```ruby
#!/usr/bin/env ruby
# Extract email addresses from text
text = ARGV[0]
email_pattern = /[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/
emails = text.scan(email_pattern)
puts emails.join("\n")
```

### Log File Analysis
```ruby
#!/usr/bin/env ruby
# Extract IP addresses from log entries
log_line = ARGV[0]
ip_pattern = /\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b/
if ip = log_line.match(ip_pattern)
    puts ip[0]
end
```

## Tasks Overview
This directory contains Ruby scripts that demonstrate various regex patterns and applications. Each script focuses on specific pattern matching scenarios commonly encountered in system administration and text processing.

## File Structure
```
0x06-regular_expressions/
├── README.md
├── 0-simply_match_school.rb
├── 1-repetition_token_0.rb
├── 2-repetition_token_1.rb
├── 3-repetition_token_2.rb
├── 4-repetition_token_3.rb
├── 5-beginning_and_end.rb
├── 6-phone_number.rb
├── 7-OMG_WHY_ARE_YOU_SHOUTING.rb
├── 100-textme.rb
└── [additional Ruby files...]
```

## Testing Your Regex

### Online Regex Testers
- [regex101.com](https://regex101.com/) - Interactive regex tester
- [regexr.com](https://regexr.com/) - Visual regex builder
- [rubular.com](http://rubular.com/) - Ruby-specific regex tester

### Command Line Testing
```bash
# Test Ruby regex
echo "test string" | ruby -ne 'puts $_ if $_ =~ /pattern/'

# Test with script
ruby script.rb "test string"
```

## Best Practices

### Writing Efficient Regex
- Keep patterns simple and readable
- Use non-capturing groups `(?:...)` when you don't need the match
- Avoid excessive backtracking with greedy quantifiers
- Use anchors to limit search scope
- Test with edge cases and large datasets

### Common Pitfalls
- **Catastrophic backtracking**: Avoid nested quantifiers like `(a+)+`
- **Greedy vs lazy matching**: Use `*?` or `+?` for lazy matching
- **Character escaping**: Remember to escape special characters
- **Unicode considerations**: Be aware of character encoding issues

### Security Considerations
- Validate regex input to prevent ReDoS (Regular Expression Denial of Service)
- Don't rely solely on regex for security validation
- Use appropriate regex engines for your use case

## Advanced Regex Features

### Lookahead and Lookbehind
```regex
(?=pattern)     # Positive lookahead
(?!pattern)     # Negative lookahead
(?<=pattern)    # Positive lookbehind
(?<!pattern)    # Negative lookbehind
```

### Named Capture Groups
```ruby
# Ruby named capture groups
pattern = /(?<year>\d{4})-(?<month>\d{2})-(?<day>\d{2})/
match = "2023-12-25".match(pattern)
puts match[:year]   # "2023"
puts match[:month]  # "12"
puts match[:day]    # "25"
```

## Debugging Regex

### Common Issues
- Pattern not matching expected strings
- Pattern matching too much or too little
- Performance issues with complex patterns
- Unicode and encoding problems

### Debugging Techniques
```ruby
# Enable debug mode for regex
pattern = /complex.*pattern/
puts pattern.inspect

# Test incrementally
simple_pattern = /simple/
complex_pattern = /complex.*pattern/

# Use match groups to isolate issues
pattern = /(part1)(part2)(part3)/
```

## Resources
- [Ruby Regular Expressions](https://ruby-doc.org/core/Regexp.html)
- [Oniguruma Documentation](https://github.com/kkos/oniguruma)
- [Regular Expressions Tutorial](https://www.regular-expressions.info/)
- [Regex Cheat Sheet](https://www.rexegg.com/regex-quickstart.html)

## License
This project is part of the ALX Software Engineering Program curriculum.