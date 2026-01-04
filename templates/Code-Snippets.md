```typescript
/ calculate color

const color = (d: NodeData) => {

const isCurrent = d.id === slug

if (isCurrent) {

return "var(--secondary)"

} else if (visited.has(d.id) || d.id.startsWith("tags/")) {

return "var(--tertiary)"

} else if (d.SimpleSlug.includes("TOPICS")) {

return "#ff00ff" // magenta

} else if (d.SimpleSlug.includes("THOUGHTS")) {

return "#00bb00" // green

} else if (d.SimpleSlug.includes("QUOTES")) {

return "#ffff55" // brightyellow

} else if (d.SimpleSlug.includes("PASSAGES")) {

return "#55555ff" // brightblue

} else { return "var(--gray)"}

}
```

```typescript
// calculate color
const color = (d: NodeData) => {

	const isCurrent = d.id === slug
	if (isCurrent) {
		return "var(--secondary)"
	} else if (visited.has(d.id) || d.id.startsWith("tags/")) {
		return "var(--tertiary)"
		} else { return "var(--gray)"}
}
```