---
layout: page
title: Search
permalink: /search/
---

<div id="search-container">
    <input type="text" id="search-input" placeholder="Search through the blog posts...">
    <div id="category-filter" style="margin-top: 1rem; display: none;">
        <span id="category-label"></span>
        <button id="clear-filter" style="margin-left: 1rem; padding: 0.25rem 0.5rem; background: #f8f9fa; border: 1px solid #dee2e6; border-radius: 4px; cursor: pointer;">Clear Filter</button>
    </div>
    <ul id="results-container"></ul>
</div>

<script src="{{ site.baseurl }}/assets/simple-jekyll-search.min.js" type="text/javascript"></script>

<script>
    let searchData = [];
    let currentCategoryFilter = null;
    
    // Load search data
    fetch('{{ site.baseurl }}/search.json')
        .then(response => response.json())
        .then(data => {
            searchData = data;
            initializeSearch();
        });

    function initializeSearch() {
        // Check for category parameter on page load
        const categoryParam = getURLParameter('category');
        if (categoryParam) {
            filterByCategory(categoryParam);
        }
        
        // Set up search input listener
        document.getElementById('search-input').addEventListener('input', performSearch);
    }

    function performSearch() {
        const query = document.getElementById('search-input').value.toLowerCase();
        const resultsContainer = document.getElementById('results-container');
        
        if (query.length === 0 && !currentCategoryFilter) {
            resultsContainer.innerHTML = '';
            return;
        }
        
        let filteredResults = searchData;
        
        // Apply category filter first
        if (currentCategoryFilter) {
            filteredResults = filteredResults.filter(post => 
                post.category.toLowerCase().includes(currentCategoryFilter.toLowerCase())
            );
        }
        
        // Apply text search if query exists
        if (query.length > 0) {
            filteredResults = filteredResults.filter(post => 
                post.title.toLowerCase().includes(query) ||
                post.category.toLowerCase().includes(query)
            );
        }
        
        // Display results
        if (filteredResults.length === 0) {
            resultsContainer.innerHTML = '<li style="color: #6c757d;">No posts found.</li>';
        } else {
            resultsContainer.innerHTML = filteredResults.map(post => `
                <div style="text-align: left !important; margin-bottom: 1.5rem; padding-bottom: 1rem; border-bottom: 1px solid #eee;">
                    <a href="${post.url}">
                        <h1 style="text-align:left !important; margin-bottom: 0.5rem;">${post.title}</h1>
                    </a>
                    <span style="text-align:left !important; color: #6c757d;">${post.date}</span><br>
                    <span style="color: #6c757d; font-size: 0.9em;">Category: ${post.category}</span>
                </div>
            `).join('');
        }
    }

    // Handle URL parameters for category filtering
    function getURLParameter(name) {
        return decodeURIComponent((new RegExp('[?|&]' + name + '=' + '([^&;]+?)(&|#|;|$)').exec(location.search) || [null, ''])[1].replace(/\+/g, '%20')) || null;
    }

    function filterByCategory(category) {
        if (category) {
            currentCategoryFilter = category;
            
            // Show category filter info
            const categoryFilter = document.getElementById('category-filter');
            const categoryLabel = document.getElementById('category-label');
            categoryLabel.textContent = 'Filtering by category: ' + category;
            categoryFilter.style.display = 'block';
            
            // Perform search with category filter
            performSearch();
        }
    }

    // Clear category filter
    document.getElementById('clear-filter').addEventListener('click', function() {
        currentCategoryFilter = null;
        document.getElementById('search-input').value = '';
        document.getElementById('category-filter').style.display = 'none';
        document.getElementById('results-container').innerHTML = '';
        
        // Update URL without category parameter
        const url = new URL(window.location);
        url.searchParams.delete('category');
        window.history.replaceState({}, '', url);
    });
</script>

<style>
#category-filter {
    background: #e7f3ff;
    border: 1px solid #b3d9ff;
    border-radius: 4px;
    padding: 0.75rem;
    margin-bottom: 1rem;
}

#clear-filter:hover {
    background: #e9ecef;
}

#results-container {
    margin-top: 1rem;
    list-style: none;
    padding: 0;
}

#search-input {
    width: 100%;
    padding: 0.75rem;
    border: 1px solid #dee2e6;
    border-radius: 4px;
    font-size: 1rem;
}

#search-input:focus {
    outline: none;
    border-color: #80bdff;
    box-shadow: 0 0 0 2px rgba(0, 123, 255, 0.25);
}
</style>