const fs = require('fs');
const path = require('path');

// Function to extract tags from Mocha tests
function extractTagsFromMochaTests(testFile) {
    const testContent = fs.readFileSync(testFile, 'utf8');
    const testLines = testContent.split('\n');

    const tags = {};

    let currentTest = null;

    // Iterate through lines to find `it()` tests and `.tags` assignment
    testLines.forEach(line => {
        // Look for the 'it' block (test function)
        const testMatch = line.match(/it\(['"](.*)['"]/);
        if (testMatch) {
            currentTest = testMatch[1];  // Capture the test description
            tags[currentTest] = [];
        }

        // Look for the '.tags' assignment on the next line
        if (line.includes('.tags')) {
            // Extract tags from the line
            const tagMatch = line.match(/\.tags = \[(.*?)\];/);
            if (tagMatch) {
                // Split the tags by comma and clean up spaces
                const tagList = tagMatch[1].split(',').map(tag => tag.trim().replace(/['"]+/g, ''));
                tags[currentTest] = tagList;
            }
        }
    });

    return tags;
}

// Usage
const tags = extractTagsFromMochaTests(path.join(__dirname, 'sample_test.js'));
console.log(tags);
