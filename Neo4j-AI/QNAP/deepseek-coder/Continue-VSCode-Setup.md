# Q:
DeepSeek-Coder:1.3b is now available from the QNAP on: [http://10.0.3.2:11434/api/](http://10.0.3.2:11434/api/) This is the Continue documentation: [https://docs.continue.dev/getting-started/overview](https://docs.continue.dev/getting-started/overview) Give step-by-step instructions on setting up the Continue extension on VSCode, including conecting to DeepSeek-Coder:1.3b on my QNAP. Use screenshots where possible.
# A:
I'll provide detailed step-by-step instructions for setting up the Continue extension in VSCode and connecting it to your DeepSeek-Coder instance on the QNAP.

# Complete Guide: Setting Up Continue Extension with DeepSeek-Coder on QNAP

## Prerequisites

- Visual Studio Code installed
- DeepSeek-Coder:1.3b running on QNAP at `http://10.0.3.2:11434/api/`
- Network access to your QNAP from your development machine

## Step 1: Install Continue Extension

### 1.1 Open VSCode Extensions

1. Launch **Visual Studio Code**
2. Click the **Extensions** icon in the sidebar (or press `Ctrl+Shift+X`)
3. In the search bar, type: `Continue`

### 1.2 Install the Extension

1. Look for **"Continue - Codestral, Claude, and more"** by Continue
2. Click the **Install** button
3. Wait for installation to complete
4. You should see a new Continue icon (∞) appear in your sidebar

_Screenshot needed: VSCode Extensions marketplace showing Continue extension_

## Step 2: Initial Continue Setup

### 2.1 Open Continue Panel

1. Click the **Continue icon (∞)** in the VSCode sidebar
2. You'll see the Continue chat interface open
3. If this is your first time, you'll see a welcome message

### 2.2 Access Configuration

1. Click the **gear icon (⚙️)** in the Continue panel
2. Alternatively, use command palette: `Ctrl+Shift+P` → type "Continue: Open config.yaml"
3. This opens the `config.yaml` file for Continue

_Screenshot needed: Continue panel with gear icon highlighted_

## Step 3: Configure DeepSeek-Coder Connection

### 3.1 Edit Configuration File

Replace the contents of `config.yaml` with this configuration:

```yaml
name: DeepSeek Local Assistant
version: 1.0.0
schema: v1

models:
  - name: DeepSeek Coder 1.3B
    provider: ollama
    model: deepseek-coder:1.3b
    apiBase: http://10.0.3.2:11434
    roles:
      - chat
      - edit
      - apply
      - autocomplete

context:
  - provider: code
  - provider: docs
  - provider: diff
  - provider: terminal
  - provider: problems
  - provider: folder
  - provider: codebase

# Optional: Performance optimizations for your Xeon D-1602
options:
  temperature: 0.2
  maxTokens: 512
  topP: 0.9
  timeout: 30000
```

### 3.2 Save Configuration

1. Save the file (`Ctrl+S`)
2. VSCode will automatically reload the Continue extension
3. You should see "DeepSeek Coder 1.3B" appear in the model dropdown

_Screenshot needed: config.yaml file open in VSCode with the configuration_

## Step 4: Test the Connection

### 4.1 Basic Chat Test

1. In the Continue panel, type a simple coding question:
    
    ```
    Write a Python function to calculate factorial
    ```
    
2. Press **Enter** or click the send button
3. You should see DeepSeek-Coder respond with code

### 4.2 Verify Model Selection

1. Click the model dropdown in Continue panel
2. Confirm "DeepSeek Coder 1.3B" is selected and active
3. You should see a green indicator showing it's connected

_Screenshot needed: Continue panel showing successful response from DeepSeek_

## Step 5: Using Continue Features

### 5.1 Inline Code Completion

1. Open any Python file (or create a new one: `test.py`)
2. Start typing code, for example:
    
    ```python
    def fibonacci(n):
    ```
    
3. Continue will automatically suggest completions
4. Press **Tab** to accept suggestions

### 5.2 Code Explanation

1. Select some code in your editor
2. Right-click and choose **"Continue: Explain Code"**
3. Or use command palette: `Ctrl+Shift+P` → "Continue: Explain Code"
4. DeepSeek will explain the selected code in the Continue panel

### 5.3 Code Generation from Comments

1. Write a comment describing what you want:
    
    ```python
    # Create a function that sorts a list of dictionaries by a specific key
    ```
    
2. Highlight the comment
3. Right-click → **"Continue: Generate Code"**
4. DeepSeek will generate the requested function

_Screenshot needed: Context menu showing Continue options_

## Step 6: Advanced Configuration Options

### 6.1 Performance Tuning

For your Xeon D-1602 setup, you can create a more optimized `config.yaml`:

```yaml
name: DeepSeek Optimized Assistant
version: 1.0.0
schema: v1

models:
  - name: DeepSeek Coder 1.3B - Chat
    provider: ollama
    model: deepseek-coder:1.3b
    apiBase: http://10.0.3.2:11434
    roles:
      - chat
      - edit
      - apply
    options:
      temperature: 0.1
      maxTokens: 256
      topP: 0.9
      timeout: 45000

  - name: DeepSeek Coder 1.3B - Autocomplete
    provider: ollama
    model: deepseek-coder:1.3b
    apiBase: http://10.0.3.2:11434
    roles:
      - autocomplete
    options:
      temperature: 0.1
      maxTokens: 128
      timeout: 15000

context:
  - provider: code
  - provider: docs
  - provider: diff
  - provider: terminal
  - provider: problems
  - provider: folder
  - provider: codebase

# Global options for performance
options:
  maxPromptTokens: 400
  debounceDelay: 300
```

### 6.2 Custom Keyboard Shortcuts

1. Go to **File** → **Preferences** → **Keyboard Shortcuts**
2. Search for "Continue"
3. Set custom shortcuts for frequently used commands:
    - `Ctrl+I`: Continue: Ask Question
    - `Ctrl+Shift+I`: Continue: Explain Code
    - `Ctrl+Alt+I`: Continue: Generate Code

_Screenshot needed: Keyboard shortcuts configuration_

## Step 7: Troubleshooting

### 7.1 Connection Issues

**Problem**: Continue can't connect to DeepSeek **Solutions**:

1. Verify QNAP is accessible: Open `http://10.0.3.2:11434` in browser
2. Check firewall settings on QNAP
3. Ensure Container Station is running the Ollama container
4. Test with curl:
    
    ```bash
    curl http://10.0.3.2:11434/api/tags
    ```
    

### 7.2 Slow Response Times

**Problem**: DeepSeek takes too long to respond **Solutions**:

1. Reduce `numPredict` in configuration (try 128-256)
2. Lower `numCtx` to 1024 or 512
3. Set `temperature` to 0.1 for faster, more deterministic responses
4. Use quantized model: `deepseek-coder:1.3b-q4_0`

### 7.3 Autocomplete Not Working

**Problem**: Tab completion doesn't appear **Solutions**:

1. Ensure `tabAutocompleteModel` is configured in `config.json`
2. Check VSCode settings: disable other autocomplete extensions temporarily
3. Increase `debounceDelay` to 500ms if it's too aggressive
4. Verify the model name exactly matches what's available on QNAP

### 7.4 Model Not Found Error

**Problem**: "Model not found" error **Solutions**:

1. Check available models on QNAP:
    
    ```bash
    curl http://10.0.3.2:11434/api/tags
    ```
    
2. Verify exact model name in configuration
3. Pull model if missing:
    
    ```bash
    docker exec -it ollama-container ollama pull deepseek-coder:1.3b
    ```
    

## Step 8: VSCode Integration Tips

### 8.1 Workspace Configuration

Create a `.vscode/settings.json` in your project:

```json
{
  "continue.enableTabAutocomplete": true,
  "continue.enableChatPredictions": true,
  "editor.quickSuggestions": {
    "other": true,
    "comments": false,
    "strings": true
  }
}
```

### 8.2 Multi-Language Support

DeepSeek-Coder supports multiple languages. Test with:

- **Python**: Most optimized
- **JavaScript/TypeScript**: Good support
- **Java, C++, Go**: Decent support
- **HTML/CSS**: Basic support

### 8.3 Git Integration

Continue works well with Git workflows:

1. Select changed code
2. Use "Continue: Explain Code" to understand modifications
3. Generate commit messages with "Continue: Generate Git Commit Message"

## Step 9: Useful Commands and Shortcuts

### 9.1 Command Palette Commands

- `Continue: Ask Question` - Open chat with highlighted code
- `Continue: Generate Code` - Generate from comments/selection
- `Continue: Explain Code` - Explain highlighted code
- `Continue: Optimize Code` - Suggest optimizations
- `Continue: Add Comments` - Add documentation
- `Continue: Find Bugs` - Code review assistance

### 9.2 Quick Actions

- **Ctrl+L**: Quick chat with current context
- **Tab**: Accept autocomplete suggestion
- **Escape**: Dismiss autocomplete
- **Ctrl+Shift+Enter**: Send message in chat

## Step 10: Best Practices

### 10.1 Effective Prompting

1. **Be specific**: Instead of "fix this", say "optimize this function for performance"
2. **Provide context**: Include relevant code or requirements
3. **Use comments**: Write clear comments for code generation
4. **Iterate**: Refine requests based on initial responses

### 10.2 Performance Optimization

1. **Use shorter prompts** for autocomplete
2. **Limit context window** for faster responses
3. **Cache models** by keeping QNAP container running
4. **Batch similar requests** to maintain model warmth

### 10.3 Security Considerations

1. **Local execution**: Code never leaves your network
2. **No telemetry**: Continue respects privacy
3. **Sensitive code**: Safe to use with proprietary projects
4. **Network isolation**: Works entirely on local network

## Verification Checklist

✅ **Installation Complete**

- [ ] Continue extension installed in VSCode
- [ ] Continue icon visible in sidebar
- [ ] Configuration file accessible

✅ **Connection Established**

- [ ] DeepSeek-Coder responding to chat
- [ ] Model dropdown shows correct model
- [ ] No connection errors in console

✅ **Features Working**

- [ ] Tab autocomplete functioning
- [ ] Code explanation working
- [ ] Code generation from comments
- [ ] Right-click context menu available

✅ **Performance Optimized**

- [ ] Response times under 5-10 seconds
- [ ] Autocomplete appears within 1-2 seconds
- [ ] No timeout errors
- [ ] QNAP CPU usage reasonable

Your Continue extension should now be fully configured and connected to DeepSeek-Coder on your QNAP! The setup provides a powerful local AI coding assistant that runs entirely on your network.

You're absolutely right to be confused! Continue has undergone a major version update. The documentation I referenced was for the older version that used `config.json`, but you have Continue 1.0.19 which uses the new `config.yaml` format.

Let me provide the correct configuration for your setup:Perfect catch! You're absolutely right. Continue 1.0.19 uses the new YAML configuration format, not JSON. Here's the key difference:

**Continue 1.0.19+ (New Format):**

- Uses `config.yaml`
- Schema v1 format
- Models have `roles` instead of separate autocomplete config
- Different structure entirely

**For your DeepSeek setup, use this `config.yaml`:**

```yaml
name: DeepSeek Local Assistant  
version: 1.0.0
schema: v1

models:
  - name: DeepSeek Coder 1.3B
    provider: ollama
    model: deepseek-coder:1.3b
    apiBase: http://10.0.3.2:11434
    roles:
      - chat
      - edit  
      - apply
      - autocomplete

context:
  - provider: code
  - provider: docs
  - provider: diff
  - provider: terminal
  - provider: problems
  - provider: folder
  - provider: codebase
```

**Key Changes in v1.0+:**

1. **Single model with multiple roles** instead of separate chat/autocomplete models
2. **YAML format** instead of JSON
3. **Schema versioning** system
4. **Built-in context providers** for better code understanding

The guide has been updated to reflect the correct v1.0.19 configuration format. Thank you for catching that - the new version is much cleaner and more powerful!