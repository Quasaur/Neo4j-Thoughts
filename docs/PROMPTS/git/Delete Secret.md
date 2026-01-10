I received the folllowing error while attempting to push the latest changes of the project /Users/Developer/DJANGO/wisdom-book :

```bash
Enumerating objects: 34, done.
Counting objects: 100% (33/33), done.
Delta compression using up to 8 threads
Compressing objects: 100% (19/19), done.
Writing objects: 100% (22/22), 7.21 KiB | 7.21 MiB/s, done.
Total 22 (delta 8), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (8/8), completed with 6 local objects.
remote: error: GH013: Repository rule violations found for refs/heads/main.
remote: 
remote: - GITHUB PUSH PROTECTION
remote:   —————————————————————————————————————————
remote:     Resolve the following violations before pushing again
remote: 
remote:     - Push cannot contain secrets
remote: 
remote:     
remote:      (?) Learn how to resolve a blocked push
remote:      https://docs.github.com/code-security/secret-scanning/working-with-secret-scanning-and-push-protection/working-with-push-protection-from-the-command-line#resolving-a-blocked-push
remote:     
remote:     
remote:       —— Anthropic API Key —————————————————————————————————
remote:        locations:
remote:          - commit: 14bf39d4d46a41222431cd63af76cd9b530a208b
remote:            path: backend/.env:1
remote:     
remote:        (?) To push, remove secret from commit(s) or follow this URL to allow the secret.
remote:        https://github.com/Quasaur/wisdom-book/security/secret-scanning/unblock-secret/30aaVrsTuKuSCffltHG6ANHpO7Q
remote:     
remote: 
remote: 
To https://github.com/Quasaur/wisdom-book.git
 ! [remote rejected] main -> main (push declined due to repository rule violations)
error: failed to push some refs to 'https://github.com/Quasaur/wisdom-book.git'
```
fix the problem and push the latest project changes to GitHub.
