<%*
// Get all markdown files in the content/THOUGHTS folder
const thoughtFolder = app.vault.getAbstractFileByPath("content/THOUGHTS");

if (!thoughtFolder) {
    new Notice("Folder content/THOUGHTS not found");
    throw new Error("Folder not found");
}

const files = app.vault.getMarkdownFiles().filter(file => 
    file.path.startsWith("content/THOUGHTS/")
);

let processedCount = 0;
let skippedCount = 0;

for (const file of files) {
    let content = await app.vault.read(file);
    
    // Look for ptopic:: inline property (with or without space)
    const ptopicMatch = content.match(/ptopic::\s*(\[\[.*?\]\]|.*?)(?=\n|$)/);
    if (!ptopicMatch) {
        skippedCount++;
        continue;
    }
    
    const ptopicValue = ptopicMatch[1].trim();
    
    // Remove the ptopic:: line
    content = content.replace(/ptopic::\s*(\[\[.*?\]\]|.*?)(?=\n|$)\n?/, '');
    
    // Handle frontmatter
    const frontmatterMatch = content.match(/^---\n([\s\S]*?)\n---/);
    
    if (frontmatterMatch) {
        const frontmatterContent = frontmatterMatch[1];
        // Check if ptopic already exists in frontmatter
        if (!frontmatterContent.includes('ptopic:')) {
            const newFrontmatter = frontmatterContent + `\nptopic: ${ptopicValue}`;
            content = content.replace(/^---\n[\s\S]*?\n---/, `---\n${newFrontmatter}\n---`);
        }
    } else {
        const newFrontmatter = `---\nptopic: ${ptopicValue}\n---\n\n`;
        content = newFrontmatter + content;
    }
    
    await app.vault.modify(file, content);
    processedCount++;
}

new Notice(`Processed ${processedCount} files, skipped ${skippedCount} files (no ptopic property)`);
_%>