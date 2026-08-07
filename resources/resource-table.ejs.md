````{=html}
<table class="table">
<thead>
<tr>
  <th>Resource</th>
  <th>Description</th>
  <th>Author or organization</th>
  <th>Type</th>
  <th>Topics</th>
  <th>Review status</th>
</tr>
</thead>
<tbody class="list">
<% for (const item of items) {
  const title = item.title || "Untitled resource";
  const description = item.description || "";
  const author = item.author_or_organization || "";
  const type = item.resource_type || "";
  const topics = Array.isArray(item.topics) ? item.topics.join(", ") : (item.topics || "");
  const reviewStatus = item.review_status || "";
  const url = typeof item.url === "string" && /^https?:\/\//i.test(item.url) ? item.url : null;
%>
<tr <%= metadataAttrs(item) %>>
  <td class="listing-title"><% if (url) { %><a href="<%= url %>"><%= title %></a><% } else { %><span><%= title %></span><br><span class="text-muted">Source link unavailable</span><% } %></td>
  <td class="listing-description"><%= description %></td>
  <td class="listing-author_or_organization"><%= author %></td>
  <td class="listing-resource_type"><%= type %></td>
  <td class="listing-topics"><%= topics %></td>
  <td class="listing-review_status"><%= reviewStatus %></td>
</tr>
<% } %>
</tbody>
</table>
````
