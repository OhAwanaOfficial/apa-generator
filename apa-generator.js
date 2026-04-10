function formatAuthors(authorInput) {
    let authors = authorInput.split(",").map(a => a.trim());

    return authors.map(a => {
        let parts = a.split(" ");
        let lastName = parts.pop();
        lastName = lastName.charAt(0).toUpperCase() + lastName.slice(1).toLowerCase();
        let initials = parts.map(p => p[0].toUpperCase() + ".").join(" ");
        return `${lastName}, ${initials}`;
    }).join(", ");
}

function generateAPA(data) {
    let authors = formatAuthors(data.author);
    let formattedTitle = formatTitle(data.title);
    let title = `<i>${formattedTitle}</i>`;

    if (data.source_type === "book") {
        let publisherPart = data.publisher ? ` ${data.publisher}.` : "";
        return `${authors} (${data.year}). ${title}.${publisherPart}`;
    }

    if (data.source_type === "website") {
        return `${authors} (${data.year}). ${title}. Retrieved from ${data.url}`;
    }

    if (data.source_type === "journal") {
        return `${authors} (${data.year}). ${title}.`;
    }

    return "Invalid source type";
}
function formatTitle(title) {
    title = title.toLowerCase();
    return title.charAt(0).toUpperCase() + title.slice(1);
}