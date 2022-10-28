<?php
  require_once 'php/db.php';
  require_once 'php/functions.php';

  $datas = get_publish_article();
?>


<!DOCTYPE html>
<html lang="zh-TW">
	<head>
		<title>article_list</title>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css"/>
		<link rel="stylesheet" href="css/style.css"/>
		<link rel="shortcut icon" href="images/favicon.ico">
	</head>


<!--event_article_id 事件表單ID-->
<!--event_title      事件表單主題-->
<!--event_content    事件表單敘述-->
<!--event_edit_date  事件編輯日期-->


	<body>
		<?php include_once 'menu.php'; ?>
		<div class="content">
			<div class="container">
				<div class="row">
					<div class="col-xs-12">
						<?php if(!empty($datas)):?>
							<?php foreach($datas as $row):?>
							<?php 
								$abstract = strip_tags($row['content']);
								$abstract = mb_substr($abstract, 0, 100, "UTF-8") 
							?>
							<div class="panel panel-primary">
						        <div class="panel-heading">
						            <h3 class="panel-title">
						            	<a href="article.php?p=<?php echo $row['id']; ?>"><?php echo $row['even_article_title']; ?></a>
						            </h3>
						        </div>
						        <div class="panel-body">
						        	<p>
						        		<span class="label label-info"><?php echo $row['category']; ?></span>&nbsp;
						        		<span class="label label-danger"><?php echo $row['event_edit_date']; ?></span>
						        	</p>
						            <?php echo $abstract; ?>
						        </div>
						    </div>
						    <?php endforeach; ?>
						<?php else: ?>
							<h3 class="text-center">No article is here</h3>
					    <?php endif; ?>
					</div>
				</div>
			</div>
		</div>
		
    <?php include_once 'footer.php'; ?>
	</body>
</html>
