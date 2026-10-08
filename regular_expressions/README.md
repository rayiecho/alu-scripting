# Regular Expressions

Ruby scripts using the Oniguruma regex engine (Ruby's default). Each script takes one argument and prints every match.

| File | Regex | What it matches |
|------|-------|-----------------|
| 0-simply_match_school.rb | `/School/` | The word "School" |
| 1-repetition_token_0.rb | `/hbt{2,5}n/` | `hb`, 2 to 5 `t`s, then `n` |
| 2-repetition_token_1.rb | `/hb?tn/` | `htn` or `hbtn` |
| 3-repetition_token_2.rb | `/hbt+n/` | `hb`, one or more `t`s, then `n` |
| 4-repetition_token_3.rb | `/hbt*n/` | `hb`, zero or more `t`s, then `n` (no square brackets) |
| 5-beginning_and_end.rb | `/^h.n$/` | Exactly `h`, any single character, `n` |
| 6-phone_number.rb | `/^\d{10}$/` | Exactly a 10-digit phone number |
| 7-OMG_WHY_ARE_YOU_SHOUTING.rb | `/[A-Z]/` | Capital letters only |
| 8-textme.rb | `/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/` | Sender, receiver and flags from TextMe logs, printed as `SENDER,RECEIVER,FLAGS` |
| 9-passed_linkedin_regex_challenge.jpg | — | Screenshot of the solved LinkedIn regex puzzle |

## Usage

```
./0-simply_match_school.rb "Best School"
School
```
