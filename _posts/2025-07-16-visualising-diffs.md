---
layout: post
title: Visualising Code Diffs
categories: [Tips]
---

When we write code we typically leverage something like Git or Mercurial to track changes we make to files. These systems make it easy to see what has changed at a glance without picking through every line of code. Personally, I use VSCode's Git integration. But who writes code themselves these days? When producing code with LLMs we still want to be able to track diffs easily. 

Let's see how it's done with two simple methods:
* VSCode native
* difflib

# VSCode

As mentioned, VSCode is great for reviewing diffs, but how can we utilise that when generating code with LLMs? Simple: create temp files out of the code and then compare using VSCode's in-built tools. The below function shows a simple example of this which outputs helpful commands to do the comparisons with each different version of a file passed in codes.

```python
import os
import tempfile

def save_versions_for_vscode_diff(codes: list[str]):
    """Save code versions as separate files for VS Code comparison"""
    if len(codes) < 2:
        print("Need at least 2 versions to compare")
        return
    
    temp_dir = tempfile.mkdtemp()
    file_paths = []
    
    for i, code in enumerate(codes):
        file_path = os.path.join(temp_dir, f'code_v{i+1}.py')
        with open(file_path, 'w') as f:
            f.write(code)
        file_paths.append(file_path)
        print(f"Saved version {i+1} to: {file_path}")
    
    print(f"\nTo compare in VS Code:")
    for i in range(1, len(file_paths)):
        print(f"code --diff {file_paths[i-1]} {file_paths[i]}")
    
    return file_paths
```

# difflib

If you don't want to use VSCode, Python also has a module specifically for this purpose. [difflib](https://docs.python.org/3/library/difflib.html) is used to compare sequences such as code and generate differences between them.

By leveraging this module, the differences in a file can be quickly seen directly in a jupyter notebook or IDE.


```python
import difflib

def compare_code_versions(codes):
    """Compare all versions of code"""
    if len(codes) < 2:
        print("Need at least 2 versions to compare")
        return
    
    for i in range(1, len(codes)):
        print(f"\n{'='*60}")
        print(f"COMPARISON: Version {i} vs Version {i+1}")
        print(f"{'='*60}")
        
        old_code = codes[i-1].splitlines(keepends=True)
        new_code = codes[i].splitlines(keepends=True)
        
        # Git-style unified diff
        diff = difflib.unified_diff(
            old_code, 
            new_code,
            fromfile=f'version_{i}',
            tofile=f'version_{i+1}',
            lineterm=''
        )
        print(''.join(diff))
```
