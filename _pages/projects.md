---
layout: page
permalink: /projects/
title: Projects
---


<div id="archives">
  <section id="archive">
     <h3>Most Recent Projects</h3>
      {% assign sorted_projects = site.projects | sort: 'date' | reverse %}
      <ul class="this">
      {% for post in sorted_projects %}
          <li>
            <b><a href="{{ site.baseurl }}{{ post.url }}">{% if post.title and post.title != "" %}{{ post.title }}{% else %}{{ post.excerpt | strip_html }}{% endif %}</a></b> - {% if post.date and post.date != "" %}{{ post.date | date: "%e %B %Y" }}{% endif %}
          </li>
      {% endfor %}
      </ul>
  </section>
</div>
