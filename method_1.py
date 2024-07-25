file_paths = [
    'static\\pdf\\01 Adsolut initiatie\\page_1.pdf', 
    'static\\pdf\\01 Adsolut initiatie\\page_10.pdf', 
    'static\\pdf\\01 Adsolut initiatie\\page_11.pdf', 
    'static\\pdf\\01 Adsolut initiatie\\page_12.pdf', 
    'static\\pdf\\01 Adsolut initiatie\\page_13.pdf', 
    'static\\pdf\\01 Adsolut initiatie\\page_14.pdf', 
    'static\\pdf\\01 Adsolut initiatie\\page_15.pdf', 
    'static\\pdf\\01 Adsolut initiatie\\page_16.pdf', 
    'static\\pdf\\01 Adsolut initiatie\\page_17.pdf', 
    'static\\pdf\\01 Adsolut initiatie\\page_18.pdf', 
    'static\\pdf\\01 Adsolut initiatie\\page_19.pdf', 
    'static\\pdf\\01 Adsolut initiatie\\page_2.pdf', 
    'static\\pdf\\01 Adsolut initiatie\\page_20.pdf', 
    'static\\pdf\\01 Adsolut initiatie\\page_21.pdf', 
    'static\\pdf\\01 Adsolut initiatie\\page_22.pdf', 
    'static\\pdf\\01 Adsolut initiatie\\page_23.pdf', 
    'static\\pdf\\01 Adsolut initiatie\\page_24.pdf', 
    'static\\pdf\\01 Adsolut initiatie\\page_25.pdf', 
    'static\\pdf\\01 Adsolut initiatie\\page_26.pdf', 
    'static\\pdf\\01 Adsolut initiatie\\page_27.pdf', 
    'static\\pdf\\01 Adsolut initiatie\\page_28.pdf', 
    'static\\pdf\\01 Adsolut initiatie\\page_29.pdf', 
    'static\\pdf\\01 Adsolut initiatie\\page_3.pdf', 
    'static\\pdf\\01 Adsolut initiatie\\page_30.pdf', 
    'static\\pdf\\01 Adsolut initiatie\\page_4.pdf', 
    'static\\pdf\\01 Adsolut initiatie\\page_5.pdf', 
    'static\\pdf\\01 Adsolut initiatie\\page_6.pdf', 
    'static\\pdf\\01 Adsolut initiatie\\page_7.pdf', 
    'static\\pdf\\01 Adsolut initiatie\\page_8.pdf', 
    'static\\pdf\\01 Adsolut initiatie\\page_9.pdf'
]

def sort_file_paths(file_paths):
  return sorted(file_paths, key=lambda x: int(x.split('_')[-1].split('.')[0]))

sorted_paths = sort_file_paths(file_paths)
print(sorted_paths)