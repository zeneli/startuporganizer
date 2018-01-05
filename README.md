# Startup Organizer
A blog focused on news relating to technology startup businesses.
The goal is to help publicize startups to blog readers.

## Project Specification
Each startup will be its own object which allows us to add special
information related to the business such as:
- listing a description and a date, or
- linking to external articles.

Each startup will have its own set of tags labels.
Tags allow for categorizing and organizing blogs in a simple, but
flexible manner.

Blog posts will exist for news about the site or to annouce news about
startups in our system.

## Behaviors Spec
The project should implement the following behaviors:
- list startup organizations
- organize startups (by tags or labels)
- link to external news sources about startups
- write blog posts about startups

## Data Model
To achieve the behaviors above, we need to store information about
four entities: startups, tags, news links, and blog posts.
The following is a list of entites and associated attributes for our
models. Each entity is a table and the associated attributes are the
corresponding columns of the table.
- Tag
  - tag name
  - slug
- Startup
  - name of company
  - slug
  - description or purpose
  - date founded
  - contact email
  - website
- News Link
  - title or headline
  - link to article
  - publication date
  - foreign key to Startup
- Blog Post
  - post title
  - slug
  - post text or description
  - publication date
- Many-to-Many Relationship
  - startup and tag
  - blog post and tag
  - blog posts and startup

### Relationships
- one-to-many, News Link to Startup: A news link
may belong to only one startup, but a startup may have multiple news
links.
- many-to-many, Startup to Tag: Each startup will have multiple tags,
and each tag may belong to multiple startups.
- many-to-many, Blog to Tag: Each blog post will have multiple tags,
and each tag may belong to multiple blog posts.
- many-to-many, Blog to Startup: Each blog post may be about multiple
startups, and each startup may be written about about multiple times.


## Features
1. a structured organization of startups according to tags
2. a blog

## List of pages.
List of webpages we will build:
1. page to list the tags
2. page to list startups
3. page to list blog posts
4. page for each tag
5. page for each startup
6. page for eac hblog post (which also lists news articles)
7. page to add a new tag
8. page to add a new startup
9. page to add a new blog post
10. page to add and connect news articles to blog posts