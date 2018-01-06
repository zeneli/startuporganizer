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
    - at most 31 characters
    - unique
  - slug
    - at most 31 characters
    - unique
- Startup
  - name of company
    - at most 31 characters
    - unique
  - slug
    - at most 31 characters
    - unique
  - description or purpose
  - date founded
  - contact email
  - website
- News Link
  - title or headline
    - at most 63 characters
  - link to article
    - at most 255 characters
  - publication date
  - foreign key to Startup
- Blog Post
  - post title
    - at most 63 characters
  - slug
    - at most 31 characters
    - unique across months
  - post text or description
  - publication date
- Many-to-Many Relationship
  - startup and tag
  - blog post and tag
  - blog posts and startup

### Relationships
1) External news articles may thus only point to a single startup
business, but any of our startup businesses may have multiple articles
written about it.
2) We allow for Startups to be categorized by Tag objects. A Tag
object may categorize many Startup objects, and Startups may be
categorized by many Tag objects.
3) Blog Posts may be about multiple Startups, just as Startups may be
written about multiple times.
4) Posts may also be categorized by multiple Tags, just as Tags may be
used multiple times o categorize different Posts.

- one-to-many, News Link to Startup: A news link
may belong to only one startup, but a startup may have multiple news
links.
- many-to-many, Startup to Tag: Each startup will have multiple tags,
and each tag may belong to multiple startups.
- many-to-many, Blog to Tag: Each blog post will have multiple tags,
and each tag may belong to multiple blog posts.
- many-to-many, Blog to Startup: Each blog post may be about multiple
startups, and each startup may be written about about multiple times.

## Model behavior
- Tags are ordered alphabetically by name.
- Startups are ordered alphabetically by name. The latest startup
should be the most recently founded startup.
- News links are ordered by descending publication date. The latest
news link is the most recently published one.
- Posts are ordered by descending publication date, then by title. The
latest post is the most recently published one.

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