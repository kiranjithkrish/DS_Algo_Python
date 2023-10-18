
function printSubArrays(arr, start, end)
{
	
	// Stop if we have reached the end
	// of the array	
	if (end == arr.length)
		return;
	
	// Increment the end point and start
	// from 0
	else if (start > end)
		printSubArrays(arr, 0, end + 1);
		
	// Print the subarray and increment
	// the starting point
	else
	{
		console.log("[");
		for(var i = start; i < end; i++)
		{
			console.log( arr[i] + ", ");
		}
		
		console.log(arr[end] + "]<br>");
		printSubArrays(arr, start + 1, end);
	}
	return;
}

// Driver code
var arr = [ 1, 2, 3 ];
printSubArrays(arr, 0, 0);

// This code is contributed by rutvik_56

