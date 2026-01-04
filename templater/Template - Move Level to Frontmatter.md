<%*
// Get all markdown files in the content folder
const contentFolder = app.vault.getAbstractFileByPath("content");

if (!contentFolder) {
    new Notice("Folder 'content' not found");
    throw new Error("Folder not found");
}

const files = app.vault.getMarkdownFiles().filter(file => 
    file.path.startsWith("content/")
);

let processedCount = 0;
let skippedCount = 0;
let alreadyInFrontmatterCount = 0;

for (const file of files) {
    let content = await app.vault.read(file);
    
    // Check if it's one of the valid types (TOPIC, THOUGHT, QUOTE, or PASSAGE)
    const typeMatch = content.match(/type::\s*(TOPIC|THOUGHT|QUOTE|PASSAGE)/) || 
                      content.match(/type:\s*(TOPIC|THOUGHT|QUOTE|PASSAGE)/);
    if (!typeMatch) {
        skippedCount++;
        continue;
    }
    
    // Look for level:: inline property (with or without space after ::)
    const levelMatch = content.match(/level::\s*(\d+|.*?)(?=\n|$)/);
    if (!levelMatch) {
        skippedCount++;
        continue;
    }
    
    const levelValue = levelMatch[1].trim();
    
    // Handle frontmatter
    const frontmatterMatch = content.match(/^---\n([\s\S]*?)\n---/);
    
    if (frontmatterMatch) {
        const frontmatterContent = frontmatterMatch[1];
        
        // Check if level already exists in frontmatter
        if (frontmatterContent.match(/level:\s*.+/)) {
            alreadyInFrontmatterCount++;
            continue;
        }
        
        // Add level to existing frontmatter
        const newFrontmatter = frontmatterContent + "\nlevel: " + levelValue;
        content = content.replace(/^---\n[\s\S]*?\n---/, "---\n" + newFrontmatter + "\n---");
    } else {
        // Create new frontmatter with level
        const newFrontmatter = "---\nlevel: " + levelValue + "\n---\n\n";
        content = newFrontmatter + content;
    }
    
    // Remove the level:: inline property from the body
    content = content.replace(/level::\s*(\d+|.*?)(?=\n|$)\n?/, '');
    
    await app.vault.modify(file, content);
    processedCount++;
}

new Notice("Processed " + processedCount + " files, skipped " + skippedCount + " files (no level property), " + alreadyInFrontmatterCount + " already in frontmatter");
_%>
