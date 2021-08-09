def hello(arr,identity):
  mapper={}
  for i in range(len(arr)):
    curr_idx=arr[i]

    for j in range(i+1,len(arr)):

        if curr_idx>=arr[j]:
            curr_idx+=1
    mapper[i]=(identity[i],curr_idx)
  res=[0]*len(arr)


  for k,v in mapper.items():
    val,idx=v
    res[idx]=val
  return res
arr=[0,1,2,1,2]
identity=[0,1,2,3,4]
print(hello(arr,identity))