---
layout: page
permalink: /categories/
title: Categories
---

<div class="categories-overview">
  <h2>Browse by Category</h2>
  <p>Click on any category to search for posts in that category.</p>
  
  <div class="category-list">
    {% assign sorted_categories = site.categories | sort %}
    {% for category in sorted_categories %}
      {% capture category_name %}{{ category | first }}{% endcapture %}
      {% assign post_count = category[1] | size %}
      <div class="category-item">
        <a href="{{ site.baseurl }}/search/?category={{ category_name | url_encode }}" class="category-link">
          <span class="category-name">{{ category_name }}</span>
          <span class="post-count">({{ post_count }} post{% if post_count != 1 %}s{% endif %})</span>
        </a>
      </div>
    {% endfor %}
  </div>
</div>

<div id="archives">
  <h2>All Posts by Category</h2>
  {% assign sorted_categories = site.categories | sort %}
  {% for category in sorted_categories %}
    <div class="archive-group">
      {% capture category_name %}{{ category | first }}{% endcapture %}
      <div id="{{ category_name | slugize }}"></div>
      
      <h3 class="category-head">{{ category_name }}</h3>
      <a name="{{ category_name | slugize }}"></a>
      {% for post in site.categories[category_name] %}
      <article class="archive-item">
        <h4><a href="{{ site.baseurl }}{{ post.url }}">{% if post.title and post.title != "" %}{{post.title}}{% else %}{{post.excerpt |strip_html}}{%endif%}</a></h4>
      </article>
      {% endfor %}
    </div>
  {% endfor %}
</div>

<style>
.categories-overview {
  margin-bottom: 2rem;
  padding-bottom: 2rem;
  border-bottom: 1px solid #eee;
}

.category-list {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  margin-top: 1rem;
}

.category-item {
  background: #f8f9fa;
  border: 1px solid #e9ecef;
  border-radius: 6px;
  padding: 0;
  transition: all 0.2s ease;
}

.category-item:hover {
  background: #e9ecef;
  transform: translateY(-1px);
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.category-link {
  display: block;
  padding: 0.75rem 1rem;
  text-decoration: none;
  color: #495057;
}

.category-link:hover {
  text-decoration: none;
  color: #495057;
}

.category-name {
  font-weight: 600;
  margin-right: 0.5rem;
}

.post-count {
  color: #6c757d;
  font-size: 0.9em;
}

.archive-group {
  margin-bottom: 2rem;
}

.category-head {
  color: #495057;
  border-bottom: 2px solid #dee2e6;
  padding-bottom: 0.5rem;
  margin-bottom: 1rem;
}
</style>