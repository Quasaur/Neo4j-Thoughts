<%*
// Get all markdown files in the content/THOUGHTS folder
const files = app.vault.getMarkdownFiles().filter(file => 
    file.path.startsWith("content/THOUGHTS/")
);

let processedCount = 0;
let skippedCount = 0;
let alreadyQuotedCount = 0;

for (const file of files) {
    let content = await app.vault.read(file);
    
    // Check if it's a THOUGHT file
    const typeMatch = content.match(/type::\s*THOUGHT/) || content.match(/type:\s*THOUGHT/);
    if (!typeMatch) {
        skippedCount++;
        continue;
    }
    
    // Check if frontmatter exists
    const frontmatterMatch = content.match(/^---\n([\s\S]*?)\n---/);
    if (!frontmatterMatch) {
        skippedCount++;
        continue;
    }
    
    const frontmatter = frontmatterMatch[1];
    
    // Look for ptopic in frontmatter
    const ptopicMatch = frontmatter.match(/ptopic:\s*(.+?)(?=\n|$)/);
    if (!ptopicMatch) {
        skippedCount++;
        continue;
    }
    
    const ptopicValue = ptopicMatch[1].trim();
    
    // Check if already has outer quotes
    if (ptopicValue.startsWith('"') && ptopicValue.endsWith('"')) {
        alreadyQuotedCount++;
        continue;
    }
    
    // Add outer quotes
    const quotedValue = `"${ptopicValue}"`;
    
    // Replace the ptopic line in frontmatter
    const newFrontmatter = frontmatter.replace(
        /ptopic:\s*.+?(?=\n|$)/,
        `ptopic: ${quotedValue}`
    );
    
    // Replace the entire frontmatter block
    content = content.replace(
        /^---\n[\s\S]*?\n---/,
        `---\n${newFrontmatter}\n---`
    );
    
    await app.vault.modify(file, content);
    processedCount++;
}

new Notice(`Processed ${processedCount} files, skipped ${skippedCount} files (no ptopic or not THOUGHT), ${alreadyQuotedCount} already quoted`);
_%>