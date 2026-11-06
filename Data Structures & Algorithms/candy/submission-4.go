func candy(ratings []int) int {
	    n := len(ratings)
		    if n <= 1 {
			        return n
					    }

						    candies := make([]int, n)
							    for i := range candies {
								        candies[i] = 1
										    }

											    // 1. 从左向右：确保右边评分高时，糖果比左边多
												    for i := 1; i < n; i++ {
													        if ratings[i] > ratings[i-1] {
															            candies[i] = candies[i-1] + 1
																		        }
																				    }

																					    // 2. 从右向左：确保左边评分高时，糖果比右边多，并累加总数
																						    sum := candies[n-1]
																							    for i := n - 2; i >= 0; i-- {
																								        if ratings[i] > ratings[i+1] {
																										            if candies[i] < candies[i+1]+1 {
																													                candies[i] = candies[i+1] + 1
																																	            }
																																				        }
																																						        sum += candies[i]
																																								    }

																																									    return sum
																																										}
																																										

