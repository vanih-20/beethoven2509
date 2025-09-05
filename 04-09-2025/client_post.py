#pip install requests
import requests
baseUrl = 'https://jsonplaceholder.typicode.com'

#read all post : GET / posts
print('Consuming: read all posts....')
response = requests.get(f'{baseUrl}/posts')
posts = response.json()
print(posts)

#read by id : GET / posts/1
print('Consuming: Read post by ID == 1....')
response = requests.get(f'{baseUrl}/posts/1')
posts = response.json()
print(posts)

# create post : POST /posts {"userId":1, "title":"Some Title", "body" : "Some Body"}
print('Consuming : create post...')
post = {"userId":1, "title":"Some Title", "body" : "Some Body"}
response = requests.post(f'{baseUrl}/posts', data = post)
createdPost = response.json()
print(createdPost)

#update post : PUT /posts/1 {"userId":1, "title":"Some Title", "body" : "Some Body"}

print('Consuming : update post...')
new_post = {"userId":1, "title":"Some Title", "body" : "Some Body"}
response = requests.post(f'{baseUrl}/posts', data = new_post)
updatedPost = response.json()
print(updatedPost)

#delete post : DELETE /posts/1
print('Consuming : delete post..')
response = requests.delete(f'{baseUrl}/posts/1')
if response.status_code == 200:
    print('Post deleted successfully')
else:
    print('Error in deleting the post')